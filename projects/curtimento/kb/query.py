#!/usr/bin/env python3
"""Base científica de curtimento: consulta, integridade e exportação SQLite.
Python stdlib, offline; não executa nem recomenda ajustes operacionais.
"""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
COLLECTIONS = (
    "sources", "processes", "chemistry", "knowledge",
    "evidence", "models", "measurements", "relations",
    "raw_material_routes", "process_matrix",
    "mass_balance_cases", "reference_ranges", "reference_formulations"
)

def load():
    result = {}
    for collection in COLLECTIONS:
        with (DATA / (collection + ".json")).open(encoding="utf-8") as stream:
            items = json.load(stream)
        if not isinstance(items, list):
            raise ValueError(f"{collection}: esperada lista JSON")
        result[collection] = items
    return result

def validate(data):
    errors = []
    ids = {}
    for collection, items in data.items():
        seen = set()
        for item in items:
            if not isinstance(item, dict):
                errors.append(f"{collection}: registro nao-objeto")
                continue
            identifier = item.get("id")
            if not isinstance(identifier, str) or not identifier:
                errors.append(f"{collection}: registro sem id")
            elif identifier in seen:
                errors.append(f"{collection}: id duplicado {identifier}")
            else:
                seen.add(identifier)
        ids[collection] = seen

    def check_ref(item, field, target, many=True):
        value = item.get(field, [] if many else None)
        refs = value if many else [value]
        if not isinstance(refs, list):
            errors.append(f"{item.get('id')}: {field} nao e lista")
            return
        for ref in refs:
            if ref is not None and ref not in ids[target]:
                errors.append(f"{item.get('id')}: referencia invalida {field}={ref}")

    for col in ("processes", "chemistry", "knowledge", "relations"):
        for item in data[col]:
            check_ref(item, "source_ids", "sources")
            if col == "knowledge":
                check_ref(item, "stage", "processes", False) if item.get("stage") in ids["processes"] else None
                if item.get("status") not in ("documentado", "inferencia_fisica"):
                    errors.append(f"{item.get('id')}: status de fato desconhecido")
                if not item.get("claim") or not item.get("limits"):
                    errors.append(f"{item.get('id')}: faltam claim e limits")
            if col == "chemistry":
                check_ref(item, "steps", "processes")
            if col == "relations":
                check_ref(item, "from", "processes", False)
                check_ref(item, "to", "processes", False)
    for item in data["models"]:
        check_ref(item, "sources", "sources")
        if not item.get("formula") or not item.get("assumptions") or not item.get("does_not_estimate"):
            errors.append(f"{item.get('id')}: metadados essenciais ausentes")
    for item in data["measurements"]:
        check_ref(item, "sources", "sources")
        if not item.get("unit") or not item.get("does_not_prove"):
            errors.append(f"{item.get('id')}: unidade ou limite ausente")
    for item in data["evidence"]:
        check_ref(item, "claim_id", "knowledge", False)
        check_ref(item, "study_source_id", "sources", False)
        if not item.get("not_interpretable_as"):
            errors.append(f"{item.get('id')}: falta limite de interpretacao")
    for item in data["raw_material_routes"]:
        check_ref(item, "source_ids", "sources")
        for ref in item.get("stage_impacts", []):
            check_ref(ref, "stage", "processes", False)
        if not item.get("initial_conditions") or not item.get("tracked_inputs"):
            errors.append(f"{item.get('id')}: missing raw-material route content")
    for item in data["process_matrix"]:
        check_ref(item, "source_id", "sources", False)
        check_ref(item, "stage", "processes", False)
        check_ref(item, "model_ids", "models")
        if not item.get("known_mechanism") or not item.get("independent_checks") or not item.get("limits"):
            errors.append(f"{item.get('id')}: incomplete process matrix")
    for item in data["mass_balance_cases"]:
        check_ref(item, "source_id", "sources", False)
        if not item.get("basis") or not item.get("source_pages"):
            errors.append(f"{item.get('id')}: faltam base e pagina da fonte")
        for stream in ("inputs", "outputs"):
            rows = item.get(stream)
            if not isinstance(rows, list) or not rows:
                errors.append(f"{item.get('id')}: {stream} sem correntes")
                continue
            amounts = [row.get("value") for row in rows]
            if any(not isinstance(value, (float, int)) for value in amounts):
                errors.append(f"{item.get('id')}: massa invalida em {stream}")
                continue
            if abs(sum(amounts) - item.get("expected_total", float('nan'))) > 1e-6:
                errors.append(f"{item.get('id')}: falha fechamento bruto {stream}")
            for row in rows:
                if row.get("dry_kg") is not None:
                    if abs(row["dry_kg"] + row.get("water_kg", 0) - row["value"]) > 1e-6:
                        errors.append(f"{item.get('id')}: falha decomposicao seca/agua {stream}")
            if "expected_dry_total" in item:
                if abs(sum(row.get("dry_kg", 0) for row in rows) - item["expected_dry_total"]) > 1e-6:
                    errors.append(f"{item.get('id')}: falha massa seca {stream}")
                if abs(sum(row.get("water_kg", 0) for row in rows) - item["expected_water_total"]) > 1e-6:
                    errors.append(f"{item.get('id')}: falha agua {stream}")
    for item in data["reference_ranges"]:
        check_ref(item, "source_id", "sources", False)
        if (not isinstance(item.get("min"), (int, float)) or
                not isinstance(item.get("max"), (int, float)) or
                item["min"] > item["max"] or not item.get("unit")):
            errors.append(f"{item.get('id')}: intervalo ou unidade invalido")
    for item in data["reference_formulations"]:
        check_ref(item, "source_id", "sources", False)
        check_ref(item, "stage", "processes", False)
        if not item.get("basis") or not item.get("basis_kg"):
            errors.append(f"{item.get('id')}: falta base de pesagem")
        for chem in item.get("items", []):
            if not isinstance(chem.get("percent_mass"), (int, float)):
                errors.append(f"{item.get('id')}: porcentagem invalida")

    for item in data["sources"]:
        if not item.get("url") or not item.get("title") or not item.get("access"):
            errors.append(f"{item.get('id')}: fonte incompleta")
    return errors

def document_text(item):
    return json.dumps(item, ensure_ascii=False, sort_keys=True)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("stats")
    bal = sub.add_parser("balance")
    bal.add_argument("case_id")
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--collection", choices=COLLECTIONS)
    b = sub.add_parser("build-db")
    b.add_argument("--output", required=True)
    a = p.parse_args()
    try:
        data = load()
        errors = validate(data)
        if errors:
            for error in errors:
                print("ERRO:", error, file=sys.stderr)
            return 1
        if a.command == "validate":
            print("OK: base consistente, refs resolvidas, campos essenciais presentes")
        elif a.command == "stats":
            for name in COLLECTIONS:
                print(f"{name}: {len(data[name])}")
        elif a.command == "balance":
            case = next((c for c in data["mass_balance_cases"] if c["id"] == a.case_id), None)
            if case is None:
                print(f"ERRO: caso desconhecido {a.case_id}", file=sys.stderr)
                return 2
            print(f"{case['id']}: {case['title']}")
            print(f"Fonte: {case['source_id']}, paginas: {', '.join(case['source_pages'])}")
            print(f"Base: {case['basis']}, unidade: {case['unit']}")
            inp = sum(x["value"] for x in case["inputs"])
            out = sum(x["value"] for x in case["outputs"])
            print(f"Entradas: {inp:g}; saidas: {out:g}; residuo: {inp-out:g}")
            if "expected_dry_total" in case:
                for metric, key in (("seca", "dry_kg"), ("agua", "water_kg")):
                    i = sum(x.get(key, 0) for x in case["inputs"])
                    o = sum(x.get(key, 0) for x in case["outputs"])
                    print(f"Massa {metric}: entrada {i:g}, saida {o:g}, residuo {i-o:g}")
            print("Saidas:")
            for item in case["outputs"]:
                print(f"  {item['name']}: {item['value']:g} ({100*item['value']/inp:.2f}% da massa de entrada)")
            print("Interpretacao:", case["interpretation"])
        elif a.command == "search":
            q = a.query.casefold()
            n = 0
            for name in COLLECTIONS:
                if a.collection and a.collection != name:
                    continue
                for item in data[name]:
                    if q in document_text(item).casefold():
                        n += 1
                        print(f"[{name}/{item['id']}] {item.get('title') or item.get('name') or item.get('claim') or item.get('substance') or item.get('formula') or item.get('reported_effect')}")
                        print("  ", document_text(item))
            print(f"TOTAL: {n}")
        elif a.command == "build-db":
            destination = Path(a.output)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists():
                destination.unlink()
            with sqlite3.connect(destination) as db:
                db.execute("CREATE TABLE entries (collection TEXT NOT NULL, id TEXT NOT NULL, text TEXT NOT NULL, payload TEXT NOT NULL, PRIMARY KEY(collection, id))")
                db.execute("CREATE INDEX search_collection ON entries(collection)")
                for name, items in data.items():
                    for item in items:
                        blob = document_text(item)
                        db.execute("INSERT INTO entries VALUES (?,?,?,?)", (name, item["id"], blob.casefold(), blob))
                db.commit()
            print(f"SQLite: {destination} ({sum(map(len,data.values()))} registros)")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
