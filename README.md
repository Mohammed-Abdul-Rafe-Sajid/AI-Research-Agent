# AI Research Assistant Agent

An autonomous multi-agent AI system that plans, retrieves, verifies, and synthesizes research information from multiple sources into structured reports.

## Features
- Multi-agent architecture using LangGraph
- Autonomous research planning
- Multi-source information retrieval
- Structured synthesis
- Claim verification & confidence scoring
- Session memory + long-term vector memory (planned)

## Architecture Overview
User Query → Intent Analyzer → Research Planner → Retrieval → Synthesis → Verification → Report Generator

## Tech Stack
- Python
- LangGraph
- Gemini (LLM)
- FAISS (Vector DB)
- FastAPI
- Streamlit

## Project Structure
See repository tree for modular agent design.

## Status
In progress — foundation complete, agent logic under development.


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
