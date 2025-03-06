class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
    

#Create a variable maxPro and store 0 initially.
#Create a variable minPrice and store the 0th index --> arr[0].
#Run a for loop over array.
#Update the min_price if the current element of the array (price) is less than min_price
#Take the difference of the minPrice with the current element of the array and compare and store the value it in maxPro.
#Return the maxPro.