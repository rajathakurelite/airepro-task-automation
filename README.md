# Airepro — Autonomous AI Engineering Pipeline

**Airepro** is an autonomous AI engineering workflow that turns a product idea into structured deliverables—PRD, skills plan, test strategy, security review, DevOps design, and MVP roadmap—using a 10-agent CrewAI pipeline.

---

## Overview

Airepro runs a sequential crew of specialized AI agents. Give it a product idea; it produces requirements, team design, test cases, security analysis, automation strategy, QA plan, architecture review, developer assignments, CI/CD design, and an MVP roadmap.

- **Company:** Airepro  
- **Stack:** [CrewAI](https://www.crewai.com/), LangChain, OpenAI  
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
- OpenAI API key

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

### 4. Configure environment

```bash
cp .env.example .env
```

Edit `.env` and set your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

---

## Run

```bash
python ai_software_factory.py
```

The crew runs with a default product idea. You’ll see each agent’s output in order; the final print is the **MVP roadmap** from the last agent.

To use your own idea, change the `inputs` in `ai_software_factory.py`:

```python
result = crew.kickoff(
    inputs={
        "idea": "Your product idea here"
    }
)
```

---

## Project structure

```
airepro-task-automation/
├── README.md           # This file
├── .env.example        # Env template (OPENAI_API_KEY)
├── .gitignore
├── requirements.txt    # crewai, langchain, openai, python-dotenv
├── ai_software_factory.py   # Crew definition and entry point
├── agents.py           # 10 Airepro agents (roles, goals, backstories)
└── tasks.py            # Task definitions and expected outputs
```

---

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key for the LLM backend. |

---

## License

See repository license file (if present).  

**Airepro** — autonomous AI engineering pipeline.
