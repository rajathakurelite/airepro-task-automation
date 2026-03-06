# Airepro — Autonomous AI Engineering Pipeline

**Airepro** is an autonomous AI engineering workflow that turns a product idea into structured deliverables—PRD, skills plan, test strategy, security review, DevOps design, and MVP roadmap—using a 10-agent CrewAI pipeline.

**Runs on Ollama with Llama 3 or DeepSeek — no OpenAI API key required.**

---

## Overview

Airepro runs a sequential crew of specialized AI agents. Give it a product idea; it produces requirements, team design, test cases, security analysis, automation strategy, QA plan, architecture review, developer assignments, CI/CD design, and an MVP roadmap.

- **Company:** Airepro  
- **Stack:** [CrewAI](https://www.crewai.com/), LangChain, Ollama (Llama 3 / DeepSeek)  
- **API:** Ollama only — uses `LLAMA_API_TOKEN` and `LLAMA_API_BASE` (no `OPENAI_API_KEY`)  
- **Input:** One product idea (e.g. “Build an AI-powered bullion trading platform with mobile app”)  
- **Output:** End-to-end engineering artifacts from PM through MVP planning  

---

## Agent pipeline

| # | Agent | Role | Deliverable |
|---|--------|------|-------------|
| 1 | PM Agent | Product Manager | Product Requirement Document (PRD) |
| 2 | Skills Agent | Skills Analyst | Required roles and team structure |
| 3 | Test Case Agent | Test Case Engineer | Functional and edge-case test scenarios |
| 4 | Security Agent | Security Analyst | Security and OWASP-oriented analysis |
| 5 | Automation Agent | Automation Engineer | Automation test strategy (e.g. pytest) |
| 6 | QA Agent | QA Strategist | Quality and validation strategy |
| 7 | Reviewer Agent | Code Reviewer | Architecture and code-quality review |
| 8 | Dev Assignment Agent | Developer Assignment Manager | Developer-to-module assignments |
| 9 | DevOps Agent | DevOps Engineer | CI/CD and deployment architecture |
| 10 | MVP Agent | MVP Planner | MVP roadmap and milestones |

Flow: **PM → Skills → Test Case → Security → Automation → QA → Reviewer → Dev Assignment → DevOps → MVP**.

---

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com/) installed and running (Llama 3 or DeepSeek pulled)

---

## Setup

### 1. Clone and enter the repo

```bash
git clone git@github.com:rajathakurelite/airepro-task-automation.git
cd airepro-task-automation
```

### 2. Virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment (no OpenAI key)

```bash
cp .env.example .env
```

For **local Ollama**, `.env.example` is already set: leave `LLAMA_API_TOKEN` as `ollama` (or empty) and `LLAMA_API_BASE=http://localhost:11434/v1`. Choose your model:

```env
# Llama 3
LLAMA_MODEL=ollama/llama3:8b

# Or DeepSeek
# LLAMA_MODEL=ollama/deepseek-r1
# LLAMA_MODEL=ollama/deepseek-llm
```

### 5. Ollama: pull the model

**Llama 3:**
```bash
ollama pull llama3:8b
```

**DeepSeek:**
```bash
ollama pull deepseek-r1
# or
ollama pull deepseek-llm
```

Ensure Ollama is running (`ollama serve` or the Ollama app).

---

## Run

```bash
python airepro.py
```

The crew runs with a default product idea. You’ll see each agent’s output in order; the final print is the **MVP roadmap** from the last agent.

To use your own idea, change `DEFAULT_IDEA` in `airepro.py` or call `main()` with an idea:

```python
from airepro import main
output = main(idea="Your product idea here")
```

---

## Project structure

```
airepro-task-automation/
├── README.md           # This file
├── .env.example        # Ollama config (LLAMA_*); no OPENAI_API_KEY
├── .gitignore
├── requirements.txt    # crewai, langchain, litellm, python-dotenv
├── config.py           # Ollama LLM (Llama 3 / DeepSeek)
├── airepro.py          # Crew definition and entry point
├── agents.py           # 10 Airepro agents (use config.llm)
└── tasks.py            # Task definitions and expected outputs
```

---

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `LLAMA_API_TOKEN` | No (local) | For local Ollama use `ollama` or leave empty. For remote Ollama, set your token. |
| `LLAMA_API_BASE` | No | Default `http://localhost:11434/v1`. Set for remote Ollama. |
| `LLAMA_MODEL` | No | Default `ollama/llama3:8b`. Use e.g. `ollama/deepseek-r1` for DeepSeek. |

**This project does not use `OPENAI_API_KEY`.**

---

## License

See repository license file (if present).  

**Airepro** — autonomous AI engineering pipeline.
