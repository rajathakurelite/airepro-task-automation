"""Airepro crew: 10 specialized agents for the autonomous engineering pipeline."""
from crewai import Agent

from config import llm

pm_agent = Agent(
    role="Product Manager",
    goal="Convert product idea into a clear Product Requirement Document",
    backstory="Senior PM experienced in building SaaS products",
    llm=llm,
    verbose=True,
)

skills_agent = Agent(
    role="Skills Analyst",
    goal="Identify required skills and team structure",
    backstory="Engineering manager skilled at team planning",
    llm=llm,
)

testcase_agent = Agent(
    role="Test Case Engineer",
    goal="Generate functional and edge case test scenarios",
    backstory="Expert QA engineer",
    llm=llm,
)

security_agent = Agent(
    role="Security Analyst",
    goal="Identify vulnerabilities and OWASP risks",
    backstory="Cybersecurity expert",
    llm=llm,
)

automation_agent = Agent(
    role="Automation Engineer",
    goal="Design automation test strategy using pytest",
    backstory="Automation architect",
    llm=llm,
)

qa_agent = Agent(
    role="QA Strategist",
    goal="Define quality strategy and validation process",
    backstory="QA leader",
    llm=llm,
)

reviewer_agent = Agent(
    role="Code Reviewer",
    goal="Review architecture and code quality",
    backstory="Senior software architect",
    llm=llm,
)

dev_assign_agent = Agent(
    role="Developer Assignment Manager",
    goal="Assign developers based on skills",
    backstory="Engineering delivery manager",
    llm=llm,
)

devops_agent = Agent(
    role="DevOps Engineer",
    goal="Define CI/CD pipeline and deployment architecture",
    backstory="Cloud infrastructure expert",
    llm=llm,
)

mvp_agent = Agent(
    role="MVP Planner",
    goal="Create a minimal viable product roadmap",
    backstory="Startup advisor",
    llm=llm,
)
