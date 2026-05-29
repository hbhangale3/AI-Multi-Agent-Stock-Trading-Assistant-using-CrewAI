from crewai import Crew

from Tasks.analyse_task import get_stock_analysis
from Tasks.trade_task import trade_decision
from Agents.analyst_agent import analyst_agent
from Agents.trader_agent import trader_agent

#creating the team that handles all

stock_crew = Crew(
    agents = [analyst_agent, trader_agent],
    tasks = [get_stock_analysis, trade_decision],#here order matters as the analyst agent needs to analyze the stock before the trader agent can make a decision
    verbose=True
)