# AI Research Agent

Project scaffold for an AI research agent with modular components.

Structure:

```
agents/
  intent.py
  planner.py
  retrieval.py
  synthesis.py
  verification.py
  report.py

graph/
  state.py
  graph.py

api/
  main.py

ui/
  app.py

evaluation/
  metrics.py

README.md
requirements.txt
.gitignore
```

Quick start:
- Install deps: `pip install -r requirements.txt`
- Run API: `uvicorn api.main:app --reload`
- Run UI: `flask --app ui.app run`

This repo contains only stubs to get started; implement agents and backends as needed.
