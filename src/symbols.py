from db_handler import DBHandler
class Symbols:
    def fetch_symbols(self):
        db_handler = DBHandler()
        symbols = db_handler.fetch_symbol_data()
        print(symbols)
        yf_stocks = []
        for stock in symbols:
            symbol = stock[0]
            stock_exchange = stock[1]
            print(f"Symbol: {symbol}, Stock Exchange: {stock_exchange}")
            yf_stock_symbol = symbol + "." + stock_exchange
            yf_stocks.append(yf_stock_symbol)
        return yf_stocks