class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two pointer appraoch
        max_profit = 0                                  # Initialize the maximum profit to 0

        for i in range(1,len(prices)):                  # Iterate through the prices array starting from the second element
            if prices[i] > prices[i-1]:                 # If the current price is greater than the previous price
                max_profit += prices[i] - prices[i-1]   # Add the difference to the max_profit
        return max_profit                               # return the total max profit