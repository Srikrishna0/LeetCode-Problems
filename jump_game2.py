class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) -1):               # Iterate through the array, but not the last element
            farthest = max(farthest, i+nums[i])     # Update the farthest reachable index

            if i == curr_end:                       # If we have reached the current end, we need to make another jump
                jumps += 1
                curr_end = farthest
        return jumps