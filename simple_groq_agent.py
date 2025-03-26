from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("Write a 5 sentence plan about creating an AI agent")