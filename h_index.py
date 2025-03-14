class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)      # Step 1: Sort the citations in descending order
        h = 0
        for i in range(len(citations)):     #Iterate through sorted citations
            if citations[i] >= i+1:
                h = i+1
            else:
                break                   # Stop if citation count is less than the paper count
        return h