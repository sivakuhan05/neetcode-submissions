class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [0 for _ in range(length)]
        min_price = prices[0]

        for i in range(1, length):
            profit = prices[i] - min_price
            dp[i] = max(profit, dp[i - 1])
            min_price = min(min_price, prices[i])

        return dp[length - 1]