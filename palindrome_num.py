# using string 
#    s = str(x)
 #   return s == s[::-1]  



# using int 

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return False
        if x % 10 == 0:
            return False
        temp = x
        numRev = 0
        ld = x % 10
        numRev = numRev * 10 + ld
        x = x // 10

        return True  
