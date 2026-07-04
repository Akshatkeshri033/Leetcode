# Last updated: 7/4/2026, 7:03:05 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        b = len(nums)//2
        return nums[b]
               
        