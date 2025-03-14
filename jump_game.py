class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Initialize the maximum reachable index
        max_index = 0
        # Iterate through the array
        for i in range(len(nums)):
            if i > max_index:        # If the current index is beyond the maximum reachable index, return False                   
                return False
            max_index = max(max_index, i + nums[i])     # update max_reach to be the maximum of the current max_reach and the sum of the current index i and the value at that index nums[i].
            if max_index >= len(nums) -1:               # If max_reach is greater than or equal to the last index, it means we can reach the end, so we return true.
                return True
        
        return True
