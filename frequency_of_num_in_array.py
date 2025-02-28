class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)    #Getting size of an array by len(arr)
        freq = [0]*n    #setting freq array with all '0' to the size 
        
        for num in arr:     #iterate through given array
            if(1 <=num <= n):       #consider only the number in range (<= size of an array) )
                freq[num-1]+=1      #increase frequency
        return freq    