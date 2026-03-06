"""Airepro tasks: from PRD through MVP roadmap."""
from crewai import Task

pm_task = Task(
    description="Create a Product Requirement Document from the idea.",
    expected_output="Structured PRD"
)

skills_task = Task(
    description="Identify required engineering roles and skills."
)

testcase_task = Task(
    description="Generate test cases including edge cases."
)

security_task = Task(
    description="Analyze potential security vulnerabilities."
)

automation_task = Task(
    description="Design automation testing strategy."
)

qa_task = Task(
    description="Create overall QA strategy."
)

review_task = Task(
    description="Review architecture and highlight improvements."
)

dev_assign_task = Task(
    description="Assign developers to project modules."
)

devops_task = Task(
    description="Design CI/CD pipeline and deployment strategy."
)

mvp_task = Task(
    description="Create MVP roadmap and milestone plan."
)