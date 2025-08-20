# Last updated: 8/20/2025, 5:50:16 PM
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31         # -2147483648
        INT_MAX = 2**31 - 1      # 2147483647
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            digit = x % 10
            x = x // 10

            # Check for overflow before pushing the digit
            if rev > (INT_MAX - digit) // 10:
                return 0
            
            rev = rev * 10 + digit
        
        return sign * rev
        