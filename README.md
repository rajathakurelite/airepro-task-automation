# Airepro — Autonomous AI Engineering Pipeline

**Airepro** turns a single product idea into full engineering deliverables using a **10-agent CrewAI pipeline** running on **Ollama** (Llama 3, DeepSeek, Phi, or any Ollama model). **No OpenAI API key is used.**

---

## What happens when you run it

1. **Crew starts** — CrewAI runs 10 agents in sequence.
2. **Each agent** gets the product idea (and prior outputs) and produces one deliverable.
3. **Agents run in order:** PM → Skills → Test Case → Security → Automation → QA → Reviewer → Dev Assignment → DevOps → MVP.
4. **Console output** is verbose: you see “Task Started”, “Agent Started”, and each agent’s text output.
5. **Final output** printed at the end is the **MVP roadmap** from the last agent.

Default product idea: *“Build an AI powered bullion trading platform with mobile app”* (you can change it).

---

## Overview

| Item | Detail |
|------|--------|
| **Company** | Airepro |
| **Stack** | CrewAI, LangChain, LiteLLM, Ollama |
| **API** | Ollama only — `LLAMA_API_TOKEN`, `LLAMA_API_BASE`, `LLAMA_MODEL` (no `OPENAI_API_KEY`) |
| **Input** | One product idea (string) |
| **Output** | PRD, skills plan, test cases, security analysis, automation strategy, QA strategy, architecture review, dev assignments, CI/CD design, MVP roadmap |

---

## Agent pipeline (order)

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

---

## Prerequisites

- **Python** 3.11 or 3.12
- **Ollama** installed and running (see below)
- **Enough RAM** for the model you choose (see “Choose a model” below)
- **No OpenAI API key** — this project does not use it

---

## Full setup and run (step by step)

### Step 1 — Install Ollama

**Linux (official script; needs sudo):**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Enter your sudo password when prompted. This installs Ollama under `/usr/local` and typically registers it in your PATH.

**macOS:** Download from [ollama.com](https://ollama.com) and open the app, or use Homebrew.

**Windows:** Download the installer from [ollama.com](https://ollama.com).

---

### Step 2 — Start Ollama

**Linux (foreground):**

```bash
ollama serve
```

Leave this terminal open, or run it in the background (`ollama serve &`). On many systems Ollama also runs as a user or system service after install.

**macOS / Windows:** Start the Ollama app from the menu. It listens on `http://localhost:11434` by default.

Check that it’s up:

```bash
curl http://localhost:11434/api/tags
```

You should see JSON (possibly an empty list of models).

---

### Step 3 — Pull a model

Pick **one** model and pull it. Use a **smaller model** if you have limited RAM (e.g. &lt; 8 GB).

| Model | Command | Approx. RAM | Use when |
|-------|--------|--------------|----------|
| **Phi** (small) | `ollama pull phi` | ~1.6 GB | Low memory (~2–4 GB free) |
| **TinyLlama** (smallest) | `ollama pull tinyllama` | ~0.6 GB | Very low memory |
| **Llama 3 8B** | `ollama pull llama3:8b` | ~4.6 GB | 8 GB+ free |
| **DeepSeek R1** | `ollama pull deepseek-r1` | ~5+ GB | 8 GB+ free |
| **DeepSeek LLM** | `ollama pull deepseek-llm` | varies | Check Ollama docs |

Example for low memory:

```bash
ollama pull phi
```

Example for better quality (more RAM):

```bash
ollama pull llama3:8b
```

---

### Step 4 — Clone the repo

```bash
git clone git@github.com:rajathakurelite/airepro-task-automation.git
cd airepro-task-automation
```

---

### Step 5 — Python virtual environment and dependencies

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

On Windows:

```cmd
.venv\Scripts\activate
```

Then:

```bash
pip install -r requirements.txt
```

---

### Step 6 — Environment variables (no OpenAI key)

```bash
cp .env.example .env
```

Edit `.env` and set the **model** to match what you pulled. Use the `ollama/` prefix.

**If you pulled `phi`:**

```env
LLAMA_API_TOKEN=ollama
LLAMA_API_BASE=http://localhost:11434/v1
LLAMA_MODEL=ollama/phi
```

**If you pulled `llama3:8b`:**

```env
LLAMA_MODEL=ollama/llama3:8b
```

**If you pulled `deepseek-r1`:**

```env
LLAMA_MODEL=ollama/deepseek-r1
```

- **Local Ollama:** `LLAMA_API_TOKEN` can be `ollama` or empty. `LLAMA_API_BASE` can be `http://localhost:11434/v1` (or `http://localhost:11434` — the code normalizes it).
- **Remote Ollama:** Set `LLAMA_API_BASE` to your server URL and `LLAMA_API_TOKEN` if the server requires auth.

---

### Step 7 — Run the project

With the venv activated and Ollama running:

```bash
python airepro.py
```

Or with the venv’s Python directly:

```bash
.venv/bin/python airepro.py
```

You should see:

- “Crew Execution Started”
- For each task: “Task Started”, “Agent Started”, then the agent’s output
- At the end: “FINAL OUTPUT:” and the MVP roadmap text

To use a **custom product idea** without editing code:

```python
from airepro import main
output = main(idea="Your product idea here")
print(output)
```

Or change `DEFAULT_IDEA` in `airepro.py` and run again.

---

## Project structure

```
airepro-task-automation/
├── README.md           # This file — full run details
├── .env.example        # Template for LLAMA_* (no OPENAI_API_KEY)
├── .env                # Your local config (create from .env.example)
├── .gitignore
├── requirements.txt    # crewai, langchain, litellm, python-dotenv, openai
├── config.py           # Builds Ollama LLM from LLAMA_* env vars
├── airepro.py          # Crew definition and entry point (run this)
├── agents.py           # 10 agents (all use config.llm)
└── tasks.py            # Task definitions and expected outputs
```

---

## Environment variables (reference)

| Variable | Required | Default | Description |
|----------|----------|--------|-------------|
| `LLAMA_API_TOKEN` | No (local) | — | For local Ollama use `ollama` or leave empty. For remote, set token. |
| `LLAMA_API_BASE` | No | `http://localhost:11434` | Ollama server URL. With or without `/v1` is fine. |
| `LLAMA_MODEL` | No | `ollama/llama3:8b` | Model name with `ollama/` prefix, e.g. `ollama/phi`, `ollama/deepseek-r1`. |

**This project does not use `OPENAI_API_KEY`.**

---

## Troubleshooting

| Issue | What to do |
|-------|------------|
| **Connection refused** to `localhost:11434` | Start Ollama: `ollama serve` or open the Ollama app. |
| **404** on API request | Ensure `.env` has `LLAMA_API_BASE=http://localhost:11434` or `http://localhost:11434/v1`. Restart the app after changing `.env`. |
| **Model requires more memory than available** (e.g. 4.6 GiB vs 2.2 GiB) | Use a smaller model: `ollama pull phi` or `ollama pull tinyllama`, and set `LLAMA_MODEL=ollama/phi` (or `ollama/tinyllama`) in `.env`. |
| **Agent starts but no / wrong output** | Confirm the model is loaded: `ollama list`. Ensure `LLAMA_MODEL` in `.env` matches a model you pulled (e.g. `ollama/phi` not `ollama/llama3:8b` if you only pulled `phi`). |
| **`OPENAI_API_KEY` is required** | You’re not using this project’s config. Run from the repo root with `python airepro.py` so `config.py` and `agents.py` (which use `config.llm`) are loaded. |
| **LiteLLM / Ollama not found** | Run `pip install -r requirements.txt` (includes `litellm`). |

---

## Quick copy-paste (after Ollama is installed and running)

```bash
# Pull a small model (good for low RAM)
ollama pull phi

# Clone and enter
git clone git@github.com:rajathakurelite/airepro-task-automation.git
cd airepro-task-automation

# Venv and deps
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Config: use phi
cp .env.example .env
# Edit .env and set: LLAMA_MODEL=ollama/phi

# Run
python airepro.py
```

---

## License

See repository license file (if present).

**Airepro** — autonomous AI engineering pipeline.
