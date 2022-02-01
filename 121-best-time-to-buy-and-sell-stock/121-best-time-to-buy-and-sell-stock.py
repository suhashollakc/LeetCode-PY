class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         buy = float('-inf') #max cash balance after buying  stock
#         sell = 0 #maximum cash balance after buying and selling a stock
        
#         for price in prices:
#             buy = max(-price,buy) #max of buying earlier or now
#             sell = max(price + buy,sell) #max of selling eaarlier or now
         
#         return sell
            
 #       Sliding Window Problem (Two Pointers)
        l,r = 0,1 #left -> Buying, right -> Selling
        maxP = 0
        
        while r < len(prices):
            #profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1
        return maxP
