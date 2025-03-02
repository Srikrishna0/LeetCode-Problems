class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n       #edge cases where k > n
        def reverse(start,end):     #helper function to reverse a sublist
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n-1)     #reverse entire array
        reverse(0, k-1)     #reverse the first k elements
        reverse(k, n-1)     #reversing the rem n-k elements

