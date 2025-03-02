class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = 0       #left pointer at 0th index which holds non zero elements

        for r in range(len(nums)):      #iterate through len(arr) and move non zero elements to left
            if nums[r] != 0:            #check if the index is not equal to zero
                nums[r], nums[l] = nums[l], nums[r]     #swap non zero elements with leftmost zeros
                l += 1                  # left pointer will move to next index


        