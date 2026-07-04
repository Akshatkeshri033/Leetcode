# Last updated: 7/4/2026, 7:02:46 PM
class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0
        