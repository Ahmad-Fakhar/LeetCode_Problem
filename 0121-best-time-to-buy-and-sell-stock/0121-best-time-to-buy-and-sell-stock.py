class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # x , y = 0, 1
        # maxprofit = 0
        # while  y< len (prices) :
        #     if  prices[x] < prices[y]:
        #         profit = prices[y] - prices[x]
        #         maxprofit = max (maxprofit,profit)
        #     else:
        #         x=y
        #     y+=1
        # return maxprofit
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: 
                left = right
            right += 1
        
        return maxProfit


        # maxprofit = 0
        # min_price = 0
        # for price in prices:
        #     min_price = min(min_price,price)
        #     maxprofit = max(maxprofit,min_price-price)
        # return maxprofit


        # max_profit = 0
        # min_price = ('inf')  # Set min_price to positive infinity initially
    
        # for price in prices:
        #      min_price = min(min_price, price)  # Update min_price if a lower price is found
        #      max_profit = max(max_profit, price - min_price)  # Calculate profit based on min_price

        # return max_profit

        