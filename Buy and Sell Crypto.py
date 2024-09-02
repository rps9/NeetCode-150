class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = prices[0]

        for i in range(1, len(prices)):
            current_profit = prices[i] - current_min
            max_profit = max(max_profit, current_profit)
            current_min = min(current_min, prices[i])

        return max_profit 
