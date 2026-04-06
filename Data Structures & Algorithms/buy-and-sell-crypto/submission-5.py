class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Start with very large number
        max_profit = 0
        
        for price in prices:
            # Update the minimum price we've seen so far
            min_price = min(min_price, price)
            
            # Calculate profit if we sell today
            profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit