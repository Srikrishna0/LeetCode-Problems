class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0                       #Pointer to track position for non-'val' elements

        for i in range(len(nums)):      # Iterate through the array
            if nums[i] != val:          # checks if index i not equal to given value
                nums[k] = nums [i]      # place the index at "k"
                k += 1                  # move the pointer "k" to next index
        return k