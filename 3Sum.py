class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue
        
            j = i+1                 # left pointer
            k = len(nums) -1        # right pointer

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
          # check for the cases
                if curr_sum > 0:              # if currsum > 0 move the right pointer to left
                    k -= 1
                elif curr_sum < 0:            # if currsum < 0 move the left pointer to right 
                    j += 1
                else:                         # if currsum is 0 then append the answer and move the left pointer to check the next elements
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:   # at the same time we also have to check this condition to move the current left pointer 
                        j += 1
        return result


