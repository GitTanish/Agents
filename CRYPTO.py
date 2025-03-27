from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from coingecko_tool import CoinGeckoTool  # <-- this must match the file name

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[CoinGeckoTool()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display crypto data.",
        "Convert common crypto symbols like BTC or ETH to CoinGecko IDs like 'bitcoin' and 'ethereum'."
    ],
    debug_mode=False
)

agent.print_response("Compare the current price, market cap, and 24h change of BTC and ETH.")
