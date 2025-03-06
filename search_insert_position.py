class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) -1

        while l <= r:
            mid = (l+r)//2              # Find the middle index

            if nums[mid] == target:
                return mid              # Target found at index mid
            elif nums[mid] < target:
                l = mid +1              # Search in the right half
            else:
                r = mid -1              # Search in the left half
        return l                        # If the loop exits without finding the target, left is the correct position where target should be inserted.