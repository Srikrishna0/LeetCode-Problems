class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ptr, t_ptr = 0,0                                  #Two pointer Appraoch   
        while s_ptr < len(s) and t_ptr < len(t):            #Loop while both pointers are within the bounds of their respective strings
            if s[s_ptr] == t[t_ptr]:                        # If the current characters match, move the `s` pointer forward
                s_ptr += 1
            t_ptr += 1                                      # Always move the `t` pointer forward to check the next character in `t`

        return s_ptr == len(s)                              # If the `s` pointer has reached the end of `s`, all characters were found in order to return the boolean
