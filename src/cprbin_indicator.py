class CPRBinIndicator:
    def execute(self,data):
        # cpn_bin should be one of long/short/sideways
        cpr_bin = "sideways"
        today_prices = data["today_prices"]
        historical_prices = data["historical_prices"]
        print(today_prices)
        print(historical_prices)

        one_day_before = historical_prices[0]
        two_day_before = historical_prices[1]

        print("onedaybeforehigh={}".format(one_day_before['high']))

        one_day_before_cpr = self.calculate_cpr(one_day_before)
        two_day_before_cpr = self.calculate_cpr(two_day_before)

        today_open_price = today_prices[0]["open"]

        if one_day_before_cpr["cprtc"] > two_day_before_cpr["cprtc"] and one_day_before_cpr["cprbc"] > two_day_before_cpr["cprbc"] and today_open_price >= one_day_before_cpr["cprtc"] and one_day_before["close"] >= one_day_before_cpr["cprtc"]:
            cpr_bin = 'long'
        elif one_day_before_cpr["cprtc"] < two_day_before_cpr["cprtc"] and one_day_before_cpr["cprbc"] < two_day_before_cpr["cprbc"] and today_open_price <= one_day_before_cpr["cprbc"] and one_day_before["close"] <= one_day_before_cpr["cprbc"]:
            cpr_bin = 'short'
        else:
            cpr_bin = 'sideways'

        # r1 = (2 * pivot) - one_day_before['low']
        # range = one_day_before['high'] - one_day_before['low']
        # r2 = pivot + range
        # r3 = r1 + range
        # r4 = r3 + r2 - r1
        # s1 = (2* pivot) - one_day_before['high']
        # s2 = pivot - range
        # s3 = s1 - range
        # s4 = s3 - (s1 - s2)
        return cpr_bin

    def calculate_cpr(self, prices):
        pivot = (prices['high'] + prices['low'] + prices['close']) / 3
        bc = (prices['high'] + prices['low']) / 2
        tc = pivot * 2 - bc
        return {
            "cprtc": max(bc, tc),
            "cprbc": min(bc, tc)
        }
