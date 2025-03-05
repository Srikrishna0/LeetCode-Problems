class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, maxi = 0,0               #init 2 vars to 0.. count var counts the consecutive 1's and "maxi" stores the max consecutives
        for i in range(len(nums)):      #iterate through the len(arr)
            if(nums[i] == 1):           #check if arr[i] is 1 then increase count to 1 else count to 0
                count += 1
            else:                       
                count = 0
            maxi = max(maxi,count)      #update maxi as highest count
        return maxi