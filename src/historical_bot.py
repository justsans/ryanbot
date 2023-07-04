from yahoo_finance_helper import YahooFinanceHelper
from symbols import Symbols

from datetime import date
class HistoricalBot:
    def execute(self):
        symbols = Symbols().fetch_symbols()

        for symbol in symbols:
            self.process_stock(symbol)
    def process_stock(self, symbol):
        yf_helper = YahooFinanceHelper()
        today = date.today()
        today_date = today.strftime("%Y-%m-%d")
        print("Processing stock.{}".format(today_date))
        yf_helper.fetch_historical_prices(symbol,today_date)

def main():
    bot = HistoricalBot()
    bot.execute()

if __name__ == "__main__":
    main()