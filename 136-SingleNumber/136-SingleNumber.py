# Last updated: 7/4/2026, 7:03:10 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor^i
        return xor