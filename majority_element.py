class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0                   # count to track occurunces
        el = None                      # set element to None
        

        for num in nums:        # iterate through each number in nums[]
            if count == 0:          # if count is '0' change the element
                el = num            # set element to the current num in array nums[]
            if num == el:           
                count += 1          # if num is the element increase count
            else:
                count -= 1          # Otherwise decrease count
        return el

