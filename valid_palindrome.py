class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0                               # Initialize two pointers left pointer at index 0
        r = len(s) -1                       # right pointer at index (len(s) -1) [which is the last index of the string] 

        while l < r:
            if not s[l].isalnum():          # Move left pointer if current char is not alphanumeric
                l += 1
                continue
            
            if not s[r].isalnum():          # Move right pointer if current char is not alphanumeric
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():     # Compare the characters at both pointers
                return False                     # Not a palindrome if characters don't match
            
            l += 1                           # Move the pointers towards the center
            r -= 1

        return True                     #If we've checked all characters and they matched, it's a palindrome