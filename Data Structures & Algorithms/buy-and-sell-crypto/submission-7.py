class Solution:
    def maxProfit(self, prices: List[int]) -> int:




















        buy_date = sell_date = max_profit = 0
        while sell_date < len(prices):
            if prices[buy_date] > prices[sell_date]:
                buy_date = sell_date
            max_profit = max(max_profit, prices[sell_date] - prices[buy_date])
            sell_date += 1

        return max_profit
