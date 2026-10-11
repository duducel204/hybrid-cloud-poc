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
    "evidence", "models", "measurements", "relations"
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
