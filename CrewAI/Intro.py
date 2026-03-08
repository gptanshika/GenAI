from crewai import Agent, Task, Crew, LLM
import os
from dotenv import load_dotenv
load_dotenv()

gemini_llm = LLM(provider="gemini",
                 model=os.getenv('Google_Gemini_version'),
                 api_key=os.getenv('Google_API_key'))

researcher = Agent(
    role = "Researcher",
    goal = "Find information about AI trends",
    backstory = "Expert in AI research with years of experience in analyzing technology trends.",
    llm = gemini_llm
)

writer = Agent(
    role = "Writer",
    goal = "Write a report about AI trends",
    backstory = "Professional writer specializing in technology and AI topics.",
    llm = gemini_llm

)

task1 = Task(description="Research AI trends",
             agent = researcher,
            expected_output="A summary of current AI trends and technologies."
)

task2 = Task(description = "Write report",
             agent = writer,
             expected_output="A report of current AI trends")

crew = Crew(
    agents = [researcher,writer],
    tasks = [task1,task2]
)

crew.kickoff()