from crewai import Crew
from agents import *
from tasks import *

crew = Crew(
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
        mvp_agent
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
        mvp_task
    ],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff(
        inputs={
            "idea": "Build an AI powered bullion trading platform with mobile app"
        }
    )

    print("\n\nFINAL OUTPUT:\n")
    print(result)