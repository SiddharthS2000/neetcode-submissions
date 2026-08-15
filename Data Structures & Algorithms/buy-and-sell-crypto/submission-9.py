class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_point = 0
        sell_point = 1
        max_profit = 0
        while sell_point < len(prices):
            if prices[buy_point] > prices[sell_point]:
                buy_point = sell_point
            max_profit = max(max_profit, prices[sell_point] - prices[buy_point])
            sell_point += 1
        return max_profit
