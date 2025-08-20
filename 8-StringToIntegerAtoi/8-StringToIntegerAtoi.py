# Last updated: 8/20/2025, 5:50:14 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check if string is empty after removing whitespaces
        if i >= n:
            return 0
        
        # Step 3: Handle sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Step 4: Convert digits to integer
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 5: Check for overflow before adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num
