import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    # Fetch stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Check if data is available
    if stock_data.empty:
        print("No data found for the specified ticker and date range.")
        return
    
    # Extract relevant columns (Open and Close prices)
    stock_prices = stock_data[['Open', 'Close']]
    
    # Print the stock data
    print(f"nStock Data for {ticker} from {start_date} to {end_date}:n")
    print(stock_prices)

def main():
    # Accept user input
    ticker = input("Enter the stock ticker symbol: ").strip().upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter the end date (YYYY-MM-DD): ").strip()

    # Fetch and display stock data
    fetch_stock_data(ticker, start_date, end_date)

if __name__ == "__main__":
    main()