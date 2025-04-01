class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1          #Two pointer Appraoch
        max_area = 0                    # take max_area as 0 initially

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)   #calculate the current area
            max_area = max(max_area, curr_area)         # storing curr_area into max_area until previous max_area > next curr_area

            if height[left] < height[right]:            # comparing indexing elements and moving pointers accordingly
                left += 1
            else:
                right -= 1
        return max_area