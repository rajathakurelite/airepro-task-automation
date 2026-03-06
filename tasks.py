"""Airepro tasks: from PRD through MVP roadmap."""
from crewai import Task

from agents import (
    pm_agent,
    skills_agent,
    testcase_agent,
    security_agent,
    automation_agent,
    qa_agent,
    reviewer_agent,
    dev_assign_agent,
    devops_agent,
    mvp_agent,
)

pm_task = Task(
    description="Create a Product Requirement Document from the idea.",
    expected_output="Structured PRD",
    agent=pm_agent,
)

skills_task = Task(
    description="Identify required engineering roles and skills.",
    expected_output="List of roles and skills needed.",
    agent=skills_agent,
)

testcase_task = Task(
    description="Generate test cases including edge cases.",
    expected_output="Test case list with edge cases.",
    agent=testcase_agent,
)

security_task = Task(
    description="Analyze potential security vulnerabilities.",
    expected_output="Security analysis and OWASP risks.",
    agent=security_agent,
)

automation_task = Task(
    description="Design automation testing strategy.",
    expected_output="Automation test strategy document.",
    agent=automation_agent,
)

qa_task = Task(
    description="Create overall QA strategy.",
    expected_output="QA strategy and validation process.",
    agent=qa_agent,
)

review_task = Task(
    description="Review architecture and highlight improvements.",
    expected_output="Architecture review and improvement suggestions.",
    agent=reviewer_agent,
)

dev_assign_task = Task(
    description="Assign developers to project modules.",
    expected_output="Developer-to-module assignment plan.",
    agent=dev_assign_agent,
)

devops_task = Task(
    description="Design CI/CD pipeline and deployment strategy.",
    expected_output="CI/CD and deployment architecture.",
    agent=devops_agent,
)

mvp_task = Task(
    description="Create MVP roadmap and milestone plan.",
    expected_output="MVP roadmap with milestones.",
    agent=mvp_agent,
)
