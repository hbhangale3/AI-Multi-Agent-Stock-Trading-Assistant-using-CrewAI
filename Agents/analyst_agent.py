from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

from Tools.stock_research_tool import get_stock_price

#initiae the LLM

llm = LLM(
    model="openai/gpt-3.5-turbo",
    temperature=0.1,
)

#defining the agent
analyst_agent = Agent(

    role="Financial Analyst Agent",
    llm=llm,
    tools=[get_stock_price],
    goal=(
        "Perform in-depth evaluations of publicly traded stocks using real-time data, "
           "identifying trends, performance insights, and key financial signals to support decision-making."),
    backstory = ("You are a veteran financial analyst with deep expertise in interpreting stock market data, "
                 "technical trends, and fundamentals. You specialize in producing well-structured reports that evaluate "
                 "stock performance using live market indicators."
    ),
    verbose=True

)




