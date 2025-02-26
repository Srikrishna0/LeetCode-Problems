class Solution(object):
    def twoSum(self, nums, target):
       # """
       # :type nums: List[int]
       # :type target: int
       # :rtype: List[int]
       # """
        num_indices = {} #Dictonary to store number and its index

        for i, n in enumerate (nums):
            comp = target - n     # Finds the required complement
            if comp in num_indices: #check if complement exists in dictionary
                return[num_indices[comp], i]    #return indices of two numbers
            num_indices[n] = i          #Store index of  the current number
        
        return[]

        