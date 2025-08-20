# Last updated: 8/20/2025, 5:49:39 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # For 0 and 1, sqrt(x) = x
        
        left, right = 1, x // 2  # sqrt(x) won't be more than x//2 when x >= 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid  # mid is a possible answer
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
