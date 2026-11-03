# Magus

Run it locally (browsers block loading JSON from a file:// page):

    python -m http.server 8000     # then open http://localhost:8000

It also works as-is on GitHub Pages.

## Adding questions

Questions live in `data/y7.json` ... `data/y11.json`, one object each:

    {
      "id": "y9-the-weimar-republic-1918-1939-06",
      "topic": "y9-the-weimar-republic-1918-1939",
      "question": "Your question?",
      "options": ["Right answer", "Wrong", "Wrong", "Wrong"],
      "answer": 0,
      "explanation": "Shown after every answer."
    }

- `id` must be unique. `topic` must match an `id` in `data/topics.json` (and the right year file).
- `answer` is the position of the correct option, starting from 0. Options are shuffled when shown.
- Any number of options (2 or more) works.
- Add or rename topics in `data/topics.json`. Topic order there is the order on screen.

Run `python validate.py` before you publish. It lists question counts per topic and any problems.
