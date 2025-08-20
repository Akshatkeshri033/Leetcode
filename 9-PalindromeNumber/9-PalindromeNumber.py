# Last updated: 8/20/2025, 5:50:12 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        x_str = str(x)
        return x_str == x_str[::-1]