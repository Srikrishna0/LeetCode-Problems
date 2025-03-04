#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        i, j = 0, 0
        res =[]
        
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        
        while i < len(a):
            if res[-1] != a[i]:
                res.append(a[i])
            i += 1
        
        while j < len(b):
            if res[-1] != b[j]:
                res.append(b[j])
            j += 1
        
        return res
