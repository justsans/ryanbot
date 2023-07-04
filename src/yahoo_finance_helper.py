import yfinance as yf
from db_handler import DBHandler

class YahooFinanceHelper:
    def fetch_historical_prices(self, symbol, end, start = "2023-01-01"):
        db_handler = DBHandler()
        historical_data = yf.download(symbol, start, end)
        # print(historical_data)
        db_handler.insert_historical_data(symbol, historical_data)

    def calculate_technicals(self, symbol, data):

    def insert_live_prices(self, symbol):
        db_handler = DBHandler()
        live_data = yf.download(symbol, period='1d', interval='5m')
        # print(live_data)
        # Insert live price data into the database
        db_handler.insert_live_data(symbol, live_data)
def main():
    # Example usage
    symbol = "HDB"  # Symbol for Apple Inc.
    start_date = "2023-01-01"
    end_date = "2023-06-24"
    yf = YahooFinanceHelper()
    stocks = yf.fetch_historical_prices(symbol,end_date, start_date)

if __name__ == "__main__":
    main()