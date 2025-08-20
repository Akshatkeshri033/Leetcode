# Last updated: 8/20/2025, 5:49:43 PM

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # Just add 1 and return
                return digits
            else:
                digits[i] = 0  # Set current digit to 0 and continue to next digit
                
        # If all digits were 9, we reach here, so return [1] + [0]*n
        return [1] + [0] * n