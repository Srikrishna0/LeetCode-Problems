class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer approach
        k = 2                           # start from 3rd index as we can allow the elements at most twice, so we are starting from 2nd element

        for i in range(2,len(nums)):    # iterate i from 2nd element (3rd index) until len(arr)
            if nums[i] != nums[k-2]:    # logic check index i not equal to (k-2)th index
                nums[k] = nums[i]       # insert the nums[i] in kth index
                k += 1                  # go to next index by 1
        return k
                

