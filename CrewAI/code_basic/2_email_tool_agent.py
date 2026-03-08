from dotenv import load_dotenv
load_dotenv()
from crewai import LLM
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool


llm = LLM(
    model = "gemini/gemini-2.5-flash",
    temperature=0.1
)

# response = llm.call("Who invented transcendental meditation.")
# print(response)

original_email = """
looping in Priya. TAS and PRX updates are in the deck. ETA for SDS integration is Friday.
Let's sync up tomorrow if SYNCBOT allows 😄. ping me if any blockers.
"""

class ReplaceJargonTool(BaseTool):
    name: str = "Replace Jargons"
    description: str = "Replace Jargons with more specific terms"

    def _run(self,email:str)->str:
        replacements = {
            "PRX": "Project Phoenix (internal AI revamp project)",
            "TAS": "technical architecture stack",
            "DBX": "client database cluster",
            "SDS": "Smart Data Syncer",
            "SYNCBOT": "internal standup assistant bot",
            "WIP": "in progress",
            "POC": "proof of concept",
            "ping": "reach out"
        }
        suggestions = []
        email_lower = email.lower()
        for jargons,replacement in replacements.items():
            if jargons.lower() in email_lower:
                suggestions.append(f"consider replacing '{jargons}' with '{replacement}'")
        return "\n".join(suggestions) if suggestions else "no jargon or internal abbreviations detected"

jt = ReplaceJargonTool()
# jt.run(original_email)

email_assitant = Agent(
    role = "email_assistant",
    goal = "Improve emails and make them sound professional and clear",
    backstory = "A highly experienced communication expert skilled in professional email writing",
    tool=[jt],
    verbose = True,
    llm = llm
)

email_task = Task(
    description= f"""Take the following rough email and rewrite it into a professional and polished
    version.
    Expand abbreviations:
    '''{original_email}'''""",
    agent=email_assitant,
    expected_output="A professional written email with proper formatting and content."

)

crew = Crew(
    tasks=[email_task],
    agents=[email_assitant],
    verbose= True
)

result = crew.kickoff()
print(result)





