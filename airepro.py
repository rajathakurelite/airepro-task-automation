"""
Airepro — Autonomous AI Engineering Pipeline.

Runs a 10-agent CrewAI crew from product idea to MVP roadmap.
Entry point: python airepro.py
"""
from crewai import Crew

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
from tasks import (
    pm_task,
    skills_task,
    testcase_task,
    security_task,
    automation_task,
    qa_task,
    review_task,
    dev_assign_task,
    devops_task,
    mvp_task,
)

DEFAULT_IDEA = "Build an AI powered bullion trading platform with mobile app"

CREW = Crew(
    agents=[
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
    ],
    tasks=[
        pm_task,
        skills_task,
        testcase_task,
        security_task,
        automation_task,
        qa_task,
        review_task,
        dev_assign_task,
        devops_task,
        mvp_task,
    ],
    verbose=True,
)


def main(idea: str | None = None) -> str:
    """Run the Airepro pipeline and return the final MVP roadmap output."""
    idea = idea or DEFAULT_IDEA
    result = CREW.kickoff(inputs={"idea": idea})
    return str(result)


if __name__ == "__main__":
    output = main()
    print("\n\nFINAL OUTPUT:\n")
    print(output)
