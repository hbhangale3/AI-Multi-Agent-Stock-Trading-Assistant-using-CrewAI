# AI Multi-Agent Stock Trading Assistant using CrewAI

## Overview

This project demonstrates how to build a **Multi-Agent AI System** using **CrewAI**, **OpenAI**, and **Yahoo Finance**.

The system consists of multiple AI agents working together to analyze stock market data and provide investment recommendations.

The application fetches live stock information using Yahoo Finance and uses specialized AI agents to:

1. Analyze stock performance.
2. Interpret market signals.
3. Recommend whether to **Buy**, **Hold**, or **Avoid** a stock.

This project serves as a practical introduction to:

* Agentic AI
* Multi-Agent Systems
* Tool Calling
* CrewAI
* Financial Analysis Workflows
* LLM Orchestration

---

# Architecture

```text
User Input
     │
     ▼
CrewAI Crew
     │
     ▼
Financial Analyst Agent
     │
     ▼
Yahoo Finance Tool
     │
     ▼
Stock Analysis
     │
     ▼
Trading Decision Agent
     │
     ▼
Buy / Hold / Avoid Recommendation
```

---

# Features

## Live Stock Market Data

Fetches real-time stock information using Yahoo Finance:

* Current Price
* Daily Price Change
* Percentage Change
* Currency Information

---

## Financial Analyst Agent

Responsible for:

* Fetching stock information
* Understanding market movement
* Summarizing stock performance
* Highlighting key observations

---

## Trading Decision Agent

Responsible for:

* Reviewing analyst findings
* Evaluating stock performance
* Generating Buy/Hold/Avoid recommendations
* Explaining reasoning in natural language

---

## Multi-Agent Workflow

Agents collaborate sequentially:

### Agent 1

Financial Analyst

Output:

```text
Stock summary
Price movement
Key observations
```

↓

### Agent 2

Trading Advisor

Output:

```text
Buy
Hold
Avoid
```

with supporting explanation.

---

# Project Structure

```text
CrewAI_multiAgent_stockTrader/
│
├── Agents/
│   ├── analyst_agent.py
│   └── trader_agent.py
│
├── Tasks/
│   ├── analyse_task.py
│   └── trade_task.py
│
├── Tools/
│   └── stock_research_tool.py
│
├── crew.py
├── main.py
├── .env
└── requirements.txt
```

---

## Folder Explanation

### Agents

Contains CrewAI agents.

Examples:

* Financial Analyst Agent
* Trading Decision Agent

Defines:

* Role
* Goal
* Backstory
* Available Tools

---

### Tasks

Contains task definitions.

Defines:

* Task description
* Expected output
* Assigned agent

Examples:

* Analyze stock performance
* Generate investment recommendation

---

### Tools

Contains reusable functions that agents can call.

Current tool:

```python
get_stock_price()
```

Uses Yahoo Finance to retrieve live stock data.

---

### crew.py

Creates the CrewAI workflow.

Responsible for:

* Registering agents
* Registering tasks
* Defining execution order

---

### main.py

Application entry point.

Responsible for:

* Accepting stock symbols
* Triggering Crew execution
* Displaying final recommendation

---

# Technologies Used

## AI Framework

* CrewAI

## LLM

* OpenAI GPT-4o Mini

## Market Data

* Yahoo Finance (yfinance)

## Environment Management

* python-dotenv

## LLM Provider Layer

* LiteLLM

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd CrewAI_multiAgent_stockTrader
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the Project

Start the application:

```bash
python main.py
```

Enter stock symbol:

```text
Enter stock symbol: AAPL
```

Example Output:

```text
Recommendation: HOLD

Current Stock Price: $310.61
Daily Change: -0.61%

The stock shows mild downward movement today.
Given the lack of strong momentum indicators, holding the position is recommended.
```

---

# Example Workflow

```text
Input:
AAPL

Agent 1:
Fetches stock data
Analyzes recent movement

Agent 2:
Evaluates analysis
Generates recommendation

Output:
HOLD
```

---

# Key Concepts Demonstrated

## Tool Calling

Agents use external Python functions to retrieve live market data.

---

## Agent Collaboration

Multiple agents specialize in different responsibilities.

---

## Prompt Engineering

Each agent receives:

* Role
* Goal
* Backstory
* Task Description
* Expected Output

to improve reasoning quality.

---

## Agentic AI

Demonstrates how modern AI systems combine:

* LLMs
* Tools
* Workflows
* Agent Collaboration

to solve real-world problems.

---

# Future Enhancements

* Technical Indicators (RSI, MACD, SMA)
* Historical Price Analysis
* Stock News Analysis
* Risk Assessment Agent
* Portfolio Management Agent
* Multi-Stock Comparison
* Sentiment Analysis using Financial News
* Streamlit Dashboard
* Autonomous Trading Simulation

---

# Learning Outcomes

Through this project, the following concepts were explored:

* CrewAI Fundamentals
* Multi-Agent Systems
* Tool Integration
* OpenAI API Usage
* Yahoo Finance API
* Agent Orchestration
* Prompt Engineering
* Financial Data Analysis
* Agentic AI Workflows

---

# Author

**Harshwardhan Ashish Bhangale**

MS Computer Engineering
San Jose State University

Passionate about AI, Distributed Systems, Backend Engineering, and Agentic AI Applications.
