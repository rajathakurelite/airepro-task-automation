# AI Software Factory (10 Agents)

This project demonstrates a simple autonomous AI engineering workflow using CrewAI.

## Agents Flow
PM Agent
→ Skills Agent
→ Test Case Agent
→ Security Agent
→ Automation Agent
→ QA Agent
→ Reviewer Agent
→ Developer Assignment Agent
→ DevOps Agent
→ MVP Agent

## Setup

1. Create Python 3.11 virtual environment
2. Install dependencies

pip install -r requirements.txt

3. Add your OpenAI key

cp .env.example .env

Edit `.env` and add your API key.

4. Run the system

python ai_software_factory.py