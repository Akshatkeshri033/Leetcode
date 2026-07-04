# Last updated: 7/4/2026, 7:02:06 PM
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftprefix = [0] * len(nums)
        rightprefix = [0] * len(nums)

        # left prefix sum
        leftprefix[0] = nums[0]
        for i in range(1, len(nums)):
            leftprefix[i] = leftprefix[i-1] + nums[i]

        # right prefix sum
        rightprefix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightprefix[i] = rightprefix[i+1] + nums[i]

        # answer array
        ans = [0] * len(nums)
        for i in range(n):
            left_sum = leftprefix[i-1] if i > 0 else 0
            right_sum = rightprefix[i+1] if i < n-1 else 0
            ans[i] = abs(left_sum - right_sum)

        return ans


        