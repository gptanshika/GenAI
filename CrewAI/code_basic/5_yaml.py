from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew, LLM
from crewai_tools import TavilySearchTool
import os
from crewai.project import task, agent , crew, CrewBase

@CrewBase
class BlogCrew():
    """Blog writing Crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/task.yaml"

    @agent
    def researcher(self)->Agent:
        return Agent(
            config = self.agents_config['research_agent'],
            tool = [TavilySearchTool()],
            verbose = True
        )
    
    @agent
    def writter(self)->Agent:
        return Agent(
            config = self.agents_config['writer_agent'],
            verbose = True)
    
    @task
    def research_task(self)->Task:
        return Task(
            config = self.tasks_config['task1'],
            agent = self.researcher()
        )
    
    @task
    def writter_task(self)->Task:
        return Task(
            config = self.tasks_config['task2'],
            agent = self.writter()
        )
    
    @crew
    def crew(self)->Crew:
        return Crew(
            agents=[self.researcher(),self.writter()],
            tasks = [self.research_task(),self.writter_task()]
        )
    

if __name__=='__main__':
    blog_crew = BlogCrew()
    blog_crew.crew().kickoff(inputs={"topic":"The master in GenAI as a Machine learning Engineer with 3 years of experience"})