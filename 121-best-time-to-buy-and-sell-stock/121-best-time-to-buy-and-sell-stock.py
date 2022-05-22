class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First, I would loop through prices and then loop further from i+ 1 to end of list
        # calculate profit and compare profit with max_profit and update in each iteration. Return max_profit.
        #Brute Force Approach O(n2) | O(1)
        # max_profit = 0
        # for i in range(len(prices) -1):
        #     for j in range(i+ 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        # return max_profit
        
        #Approach 2: One Pass
        min_price  =float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
                
        
        
        