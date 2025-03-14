class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""           # edge case given
        
        strs.sort()             # by sorting we can know how many strings have similar prefix 
        first = strs[0]         # take the 0th index in strs array as first and last index[-1th] as last
        last = strs[-1]
        i = 0                   # take the pointer i as 0 which acts as index in each string in array

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i +=1
        return first[:i]        # returns first 'i' elements (prefix) in the strings
