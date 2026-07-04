# Last updated: 7/4/2026, 7:02:51 PM


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] != 1:   # found a gap
                return nums[i] + 1
        if nums[0] != 0:
            return 0
        return len(nums)
