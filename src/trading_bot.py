from symbols import Symbols
from yahoo_finance_helper import YahooFinanceHelper
from db_handler import DBHandler
from cprbin_indicator import CPRBinIndicator
from datetime import date

class TradingBot:
    def execute(self):
        symbols = Symbols().fetch_symbols()
        yf_helper=YahooFinanceHelper()
        db = DBHandler()
        cprBinIndicator = CPRBinIndicator()
        today = date.today()
        today_date = today.strftime("%Y-%m-%d")
        for symbol in symbols:
            yf_helper.insert_live_prices(symbol)
            today_prices = db.fetch_today_prices(symbol)
            historical_prices = db.fetch_historical_prices(symbol, '2023-06-22')
            data = {
                "today_prices": today_prices,
                "historical_prices": historical_prices
            }
            cprbin = cprBinIndicator.execute(data)
            db.upsert_technical_indicators(symbol, today_date, cprbin )

def main():
    # Example usage
    bot = TradingBot()
    bot.execute()

if __name__ == "__main__":
    main()