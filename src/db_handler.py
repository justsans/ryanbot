import psycopg2

class DBHandler:
    def __init__(self):
        self.host = "localhost"
        self.database = "postgres"
        self.user = "sebastine"
        self.password = "Sancho@5"
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def execute_query(self, query, params=None):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()
        cur.close()

    def insert_historical_data(self, symbol, data):
        self.connect()
        cur = self.conn.cursor()

        for index, row in data.iterrows():
            cur.execute("""
                    INSERT INTO historical_data (symbol, date, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (symbol, date) DO UPDATE
                    SET open = excluded.open, high = excluded.high, low = excluded.low,
                        close = excluded.close, volume = excluded.volume
                """, (symbol, index, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))

        self.conn.commit()
        cur.close()
        self.disconnect()

    def insert_live_data(self, symbol, data):
        self.connect()
        latest_data = data.tail(1)  # Get the latest row of data
        timestamp = latest_data.index[0]
        open_price = int(latest_data['Open'].values[0])
        high_price = int(latest_data['High'].values[0])
        low_price = int(latest_data['Low'].values[0])
        close_price = int(latest_data['Close'].values[0])
        volume = int(latest_data['Volume'].values[0])

        query = """
            INSERT INTO live_data (symbol, timestamp, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (symbol)
            DO UPDATE SET open = excluded.open, high = excluded.high, low = excluded.low,
                          close = excluded.close, volume = excluded.volume, timestamp = excluded.timestamp
        """
        cur = self.conn.cursor()
        cur.execute(query, (symbol, timestamp, open_price, high_price, low_price, close_price, volume))
        self.conn.commit()
        cur.close()
        self.disconnect()

    def upsert_technical_indicators(self, symbol, date, cprbin):
        self.connect()
        query = """
            INSERT INTO technical_indicators (symbol, date, cprbin)
            VALUES (%s, %s, %s)
            ON CONFLICT (symbol, date)
            DO UPDATE SET cprbin = excluded.cprbin
        """

        cur = self.conn.cursor()
        self.execute_query(query, (symbol, date, cprbin))
        self.conn.commit()
        cur.close()
        self.disconnect()

    def fetch_symbol_data(self):
        self.connect()
        query = "SELECT symbol,stockexchange FROM stock_symbols where active=true"
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        self.disconnect()
        return rows


    def fetch_today_prices(self, symbol):
        self.connect()
        query = "SELECT symbol, open, high, low, close, volume FROM live_data where symbol='"+ symbol + "'"
        cur = self.conn.cursor()
        cur.execute(query)
        column_Names = cur.description
        result = [{column_Names[index][0]: column for index, column in enumerate(value)} for value in cur.fetchall()]
        cur.close()
        self.disconnect()
        return result

    def fetch_historical_prices(self, symbol, maxDate=None):
        self.connect()
        query = "SELECT symbol, date, open, high, low, close, volume FROM historical_data where symbol='"+ symbol + "'"
        if maxDate:
            query = query + " and date <='" +  maxDate+"' "
        query= query + " ORDER BY date desc"
        cur = self.conn.cursor()
        cur.execute(query)
        column_Names = cur.description
        result = [{column_Names[index][0]: column for index, column in enumerate(value)} for value in cur.fetchall()]
        cur.close()
        self.disconnect()
        return result