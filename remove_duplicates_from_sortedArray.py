class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1                           #first element at 0th index is always unique
        for r in range(1,len(nums)):    # r starts from 1st index to len(arr), because l is already in the 0th index
            if nums[r] != nums[r -1]:   # checks curr element nums[r] is not equal to previous element with this formula
                nums[l] = nums[r]       #if unique value, then update left value to new right value
                l += 1                  # l is moving forward only if the new value is unique, so l should be calculating k elements
        return l                        # return l "number of elements"