# Capstone starter: Q&A over your own documents

Small Flask app. Retrieval is BM25 (no extra paid service); answers come from Claude, grounded in the retrieved chunks.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # then export the values, or: export ANTHROPIC_API_KEY=...
python ingest.py                # builds index.json from data/*.md and data/*.txt
python app.py                   # http://127.0.0.1:5000
```
No key set? It runs in demo mode and shows the passages it found.

Deploy: push to GitHub, create a Railway project from the repo, add `ANTHROPIC_API_KEY` under Variables, generate a domain. The Procfile is already set. `index.json` is rebuilt on first start.

Ideas to extend (ask Claude in chat to help): a login per customer, per-customer document folders, embeddings via a provider such as Voyage AI, an eval script that runs your 5 test questions.
