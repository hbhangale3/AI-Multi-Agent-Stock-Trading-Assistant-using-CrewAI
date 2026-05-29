import yfinance as yf
from crewai.tools import tool


#use the decorator to create a tool and define a function that fetches live data
@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol: str)-> str:
    """
    Fetches the current stock price for the given stock symbol using yfinance.
    
    Args:
        stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, GOOGL).
    
    Returns:
        str: The current stock price.
    """
    stock = yf.Ticker(stock_symbol)
    info = stock.info
    # print(info)
    current_price = info.get("regularMarketPrice")
    change=info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency","USD")
    if current_price is None:
        return f"Could not fetch data for {stock_symbol}"
    
    return(
        f"Stock: {stock_symbol}\n"
        f"Price: {current_price} {currency}\n"
        f"Change: {change} ({change_percent:.2f}%)\n"
    )



#lets test the tool 

# print(get_stock_price("AAPL"))