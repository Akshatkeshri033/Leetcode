# Last updated: 7/4/2026, 7:02:55 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # to track numbers already seen
        
        while n != 1:
            if n in seen:  # cycle detected
                return False
            seen.add(n)
            
            n = sum(int(digit)**2 for digit in str(n))  # sum of squares of digits
        
        return True
