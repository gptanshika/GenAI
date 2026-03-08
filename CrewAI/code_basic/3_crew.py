from dotenv import load_dotenv
load_dotenv()
from crewai import LLM
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool


llm = LLM(
    model = "gemini/gemini-2.5-flash",
    temperature=0.1
)

research_agent = Agent(
    role = "Research Specialist",
    goal = "Research interesting fact about the topic : {topic}",
    backstory = "You are an expect at finding relevant and factual data.",
    verbose = True,
    llm = llm
)

writer_agent = Agent(
    role = "Creative Writer",
    goal = "Write a short blog summary using the research",
    backstory = "You are skilled at writing engaging summaries based on proved content " ,
    llm = llm,
    verbose = True
)

task1 = Task(
    description =" Find 3-5 interesting and recent facts about {topic}.",
    expected_output= "A bullet list pf 3-5 facts",
    agent = research_agent
)

task2 = Task(
    description= "Write a 100-word blog post summary about {topic} using the facts from the research.",
    expected_output="A blog post summary.",
    agent =  writer_agent,
    context = [task1]
)

crew = Crew(
    tasks = [task1,task2],
    agents = [research_agent,writer_agent],
    verbose = True
)

result = crew.kickoff(inputs = {'topic':"The future of electrical vehicles"})
print(result)