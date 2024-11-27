import requests
from prettytable import PrettyTable

API_KEY = "JN4P01PMVGKPBKKT"
BASE_URL = "https://www.alphavantage.co/query"

portfolio = {}

def fetch_stock_price(symbol):
    """Fetch the latest stock price for the given symbol."""
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        price = float(data["Global Quote"]["05. price"])
        return price
    except KeyError:
        print(f"Could not fetch data for {symbol}. Check the symbol or try again later.")
        return None

def add_stock(symbol, quantity):
    """Add a stock to the portfolio."""
    price = fetch_stock_price(symbol)
    if price:
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol} at ${price:.2f} per share.")

def remove_stock(symbol, quantity):
    """Remove a stock from the portfolio."""
    if symbol in portfolio:
        if portfolio[symbol] > quantity:
            portfolio[symbol] -= quantity
            print(f"Removed {quantity} shares of {symbol}. Remaining: {portfolio[symbol]} shares.")
        elif portfolio[symbol] == quantity:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol} from the portfolio.")
        else:
            print(f"You only own {portfolio[symbol]} shares of {symbol}. Cannot remove {quantity} shares.")
    else:
        print(f"{symbol} is not in your portfolio.")

def show_portfolio():
    """Display the current portfolio with real-time prices."""
    if not portfolio:
        print("Your portfolio is empty.")
        return
    
    table = PrettyTable(["Stock", "Shares", "Price (USD)", "Value (USD)"])
    total_value = 0.0

    for symbol, quantity in portfolio.items():
        price = fetch_stock_price(symbol)
        if price:
            value = price * quantity
            total_value += value
            table.add_row([symbol, quantity, f"${price:.2f}", f"${value:.2f}"])

    print(table)
    print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    print("Welcome to the Stock Portfolio Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            symbol = input("Enter the stock symbol (e.g., AAPL, TSLA): ").upper()
            try:
                quantity = int(input("Enter the quantity: "))
                add_stock(symbol, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif choice == "2":
            symbol = input("Enter the stock symbol to remove: ").upper()
            try:
                quantity = int(input("Enter the quantity to remove: "))
                remove_stock(symbol, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
