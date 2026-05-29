from crewai import Agent, LLM
from dotenv import load_dotenv
import os
load_dotenv()

llm = LLM(
    model="openai/gpt-3.5-turbo",
    temperature=0.1,
)

trader_agent = Agent(
    role="Stock Trader Agent",
    llm=llm,
    tools=[],
    goal= (
        "Decide whether to Buy, Sell, or Hold a given stock based on live market data, "
        "price movements, and financial analysis with the available data."
    ),
    backstory = (
        "You are a strategic trader with years of experience in timing market entry and exit points. "
        "You rely on real-time stock data, daily price movements, and volume trends to make trading decisions "
        "that optimize returns and reduce risk."
    ),
    verbose=True
)

