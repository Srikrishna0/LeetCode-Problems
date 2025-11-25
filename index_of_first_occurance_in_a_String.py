class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:      # Return 0 if needle is an empty string (edge case)
            return 0
        
        for i in range(len(haystack) - len(needle) +1):  # Check each possible starting position in haystack
            if haystack[i: i+len(needle)] == needle:         # If the substring from the current position matches needle, return the position
                return i
        return -1                                       # If needle is not found, return -1