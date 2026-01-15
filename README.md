# 🧠 Agentic AI Research Assistant

An end-to-end, agent-based AI system designed to autonomously conduct
exploratory academic research.

Given a high-level research question, the system plans a research strategy,
retrieves relevant literature, stores evidence in vector memory, synthesizes
findings, verifies claims, and generates a structured, academic-style report.

The project focuses on **correctness, grounding, and transparency** rather than
fast or conversational answers. When sufficient evidence is unavailable, the
system explicitly reports uncertainty instead of hallucinating results.



## ❓ Problem Statement

Early-stage academic research is often time-consuming and error-prone.
Researchers and students typically spend significant effort on:

- Identifying relevant literature
- Filtering unrelated or low-quality sources
- Understanding architectural or methodological differences across papers
- Avoiding overconfident conclusions when evidence is incomplete

While modern Large Language Models can generate fluent answers, they often:
- Hallucinate facts or metrics
- Fail to distinguish between weak and strong evidence
- Provide confident conclusions without proper grounding

This project addresses these issues by framing research as a **multi-agent
process**, where each agent is responsible for a specific, verifiable step in
the research workflow.



## 🎯 Intended Use Cases

This system is designed for **analytical and exploratory research tasks**, not
for casual question answering.

It is well-suited for:

- Survey-style research questions  
  *e.g., “Recent approaches to medical image classification”*

- Comparative analysis  
  *e.g., “CNNs vs Vision Transformers for medical image classification”*

- Research gap identification  
  *e.g., “Limitations of Vision Transformers in low-data medical settings”*

- Early-stage literature reviews for students and researchers

The agent automates the **first 60–70% of a literature review**, allowing users
to quickly understand what is known, what is uncertain, and where evidence is
missing.



## 🚫 Non-Goals

This project intentionally avoids certain types of tasks.

It is **not** designed to:

- Act as a general-purpose chatbot
- Answer simple factoid or trivia questions  
  *(e.g., “What is a CNN?”)*

- Provide coding help or implementation tutorials
- Recommend a “best” model or tool without sufficient evidence
- Produce definitive conclusions when literature is inconclusive

If evidence is fragmented or insufficient, the system will explicitly state
this rather than generate speculative or unsupported answers.



## 🏗️ System Architecture

The system is implemented as a **multi-agent pipeline** using LangGraph.
Each agent operates on a shared state and is responsible for a clearly defined
stage of the research workflow.

The architecture follows a linear but inspectable flow, allowing intermediate
outputs (plans, sources, notes, flags) to be examined independently.

User Query
   ↓
Intent Agent
   ↓
Planner Agent
   ↓
Retrieval Agent ──→ PDF Download & Parsing
   ↓
Memory Agent (Embeddings + FAISS)
   ↓
Synthesis Agent
   ↓
Verification Agent
   ↓
Report Agent
   ↓
Final Research Report


This modular design ensures that failures or uncertainties at one stage do not
silently propagate. Each agent can surface incomplete or weak evidence explicitly.



## 🤖 Agent Responsibilities

Each agent in the system has a **single, well-defined responsibility**.

### Intent Agent
- Interprets the user’s natural language query
- Extracts the research goal, domain, task type, and desired depth
- Prevents ambiguous or poorly scoped research tasks

### Planner Agent
- Breaks the research goal into structured, logical steps
- Produces a high-level research plan rather than search queries
- Ensures the workflow follows a research-oriented sequence

### Retrieval Agent
- Retrieves relevant academic literature from ArXiv
- Downloads and parses full research papers (PDFs)
- Prioritizes breadth over precision at this stage

### Memory Agent
- Converts retrieved documents into vector embeddings
- Stores embeddings in a FAISS index
- Enables semantic retrieval for downstream reasoning

### Synthesis Agent
- Analyzes retrieved evidence and produces structured research notes
- Focuses on comparisons, strengths, limitations, and trends
- Avoids numerical claims unless explicitly supported by evidence

### Verification Agent
- Evaluates synthesized notes for unsupported or speculative claims
- Flags weak or unverifiable statements
- Enforces conservative, evidence-aware reasoning

### Report Agent
- Generates a structured, academic-style research report
- Integrates verified notes and surfaced limitations
- Explicitly communicates uncertainty where applicable



## 🔄 End-to-End Data Flow

The system operates on a shared research state that is incrementally enriched
by each agent.

1. **User Query**
   - A high-level research question is provided via the CLI.

2. **Intent & Planning**
   - The query is transformed into a structured research scope and plan.

3. **Literature Retrieval**
   - Relevant research papers are retrieved and parsed into raw text.

4. **Vector Memory Construction**
   - Document content is embedded and indexed using FAISS.

5. **Evidence Synthesis**
   - Relevant content is synthesized into structured research notes.

6. **Verification**
   - Claims are evaluated for strength and evidentiary support.

7. **Report Generation**
   - A final academic-style report is produced from verified notes.

At each stage, intermediate artifacts (plans, sources, notes, flags) remain
accessible, enabling inspection, debugging, and extension.



## 💻 Command-Line Usage

The system is accessed via a command-line interface.

### Basic Usage

```bash
python -m api.main --query "CNN vs Vision Transformers for medical image classification"
```

The query should be phrased as a research question, not a casual prompt.

The system executes the full research pipeline and outputs a structured
academic-style report to the console.



---
## 📌 Example Queries

The following query patterns work well:

- Survey-style questions  
  `Survey of OCR techniques for handwritten medical prescriptions`

- Comparative analysis  
  `CNNs vs Vision Transformers for medical image classification`

- Research gaps  
  `Limitations of Vision Transformers in low-data medical settings`

### Example Output

The generated report typically includes:
- An abstract summarizing the research context
- Structured comparison points
- Strengths and limitations derived from evidence
- Explicit acknowledgment of missing or insufficient data



## 🧠 Key Design Decisions

- **Multi-agent architecture** was chosen to decompose research into verifiable steps.
- **Vector memory (FAISS)** enables semantic grounding instead of keyword matching.
- **Verification stage** prevents unsupported claims from propagating.
- **Conservative reporting** was prioritized over confident but ungrounded answers.
- **Academic tone** was chosen to match research workflows rather than chat interfaces.



## 🛠️ Problems Faced & Fixes

- **Hallucinated or ungrounded outputs from LLMs**  
  *Fix:* Introduced a verification agent that flags weak or unsupported claims.

- **Irrelevant literature retrieval**  
  *Fix:* Tightened retrieval queries and decoupled planning language from search queries.

- **Schema mismatches between agents**  
  *Fix:* Implemented defensive parsing to support multiple data formats across agents.

- **LLM API instability and quota limits**  
  *Fix:* Added conservative prompting, reduced token usage, and fail-safe guards.

- **Framework return-type mismatches (LangGraph)**  
  *Fix:* Adapted CLI to correctly handle dictionary-based state returns.



## ⚠️ Limitations

- Retrieval quality depends on available academic literature.
- Some domains lack direct benchmark comparisons.
- The system does not provide recommendations or prescriptive advice.
- Handwritten or niche domains may produce fragmented evidence.
- No real-time web browsing beyond academic sources.




## 🔮 Future Improvements

- Domain-specific retrieval filters (e.g., medical datasets, CV subfields)
- Citation-aware report generation
- Interactive UI for inspecting intermediate agent outputs
- Support for additional scholarly databases
- Quantitative benchmark extraction where available




## 🧰 Tech Stack

- Python 3
- LangGraph
- Google Gemini API
- FAISS
- ArXiv API
- Pydantic




## 📌 Project Status

The core agentic research pipeline is complete and functional.
The project is considered stable and suitable for academic exploration,
demonstration, and further extension.
