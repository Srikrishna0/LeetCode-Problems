class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_ptr = 0
        r_ptr = len(numbers) -1                             # Two Pointer Approach

        while l_ptr < r_ptr:    
            current_sum = numbers[l_ptr] + numbers[r_ptr]   # add two pointers if l < r

            if current_sum == target:
                return [l_ptr +1, r_ptr +1]                 # Return the 1-based indices if the sum matches the target   
            elif current_sum < target:                      # Move left pointer right to increase the sum
                l_ptr += 1
            else:
                r_ptr -= 1                                  # Move right pointer left to decrease the sum
            
        return[-1,-1]                                       # Edge Case of the given problem