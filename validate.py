"""Check the Magus question files before you publish them. Run: python validate.py"""
import json, sys, pathlib
base = pathlib.Path(__file__).parent / "data"
topics = {t["id"]: t for t in json.loads((base / "topics.json").read_text(encoding="utf-8"))}
seen, problems, counts = set(), [], {}
for y in range(7, 12):
    f = base / f"y{y}.json"
    if not f.exists():
        continue
    for q in json.loads(f.read_text(encoding="utf-8")):
        qid = q.get("id", "?")
        if qid in seen: problems.append(f"{qid}: duplicate id")
        seen.add(qid)
        if q.get("topic") not in topics: problems.append(f"{qid}: unknown topic '{q.get('topic')}'")
        elif topics[q["topic"]]["year"] != y: problems.append(f"{qid}: topic belongs to year {topics[q['topic']]['year']}, file is y{y}.json")
        opts = q.get("options", [])
        if not q.get("question"): problems.append(f"{qid}: missing question")
        if len(opts) < 2: problems.append(f"{qid}: needs at least 2 options")
        if len(set(opts)) != len(opts): problems.append(f"{qid}: repeated option text")
        if not isinstance(q.get("answer"), int) or not 0 <= q["answer"] < len(opts): problems.append(f"{qid}: answer index out of range")
        if not q.get("explanation"): problems.append(f"{qid}: missing explanation")
        counts[q.get("topic")] = counts.get(q.get("topic"), 0) + 1
for t in topics.values():
    print(f"{counts.get(t['id'], 0):3}  Y{t['year']}  {t['title']}")
print("\n" + ("\n".join(problems) if problems else "All questions valid."))
sys.exit(1 if problems else 0)
