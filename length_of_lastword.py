class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0          #initial length to be '0'
        i = len(s) -1       # take pointer i which starts the indexing of the string from backwards

        while i >= 0 and s[i] == " ":  #check if the pointer index is equal to empty space
            i -= 1          # if yes then move to next step by -1 (back stepping)
        
        while i >= 0 and s[i] != " ":   #check if string index not equal to empty space
            length += 1                 #increase length by 1
            i -= 1                      # move the index to next step by -1 (backward)
        return length