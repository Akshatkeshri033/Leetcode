# Last updated: 8/20/2025, 5:49:37 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2  # f(1)=1, f(2)=2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b