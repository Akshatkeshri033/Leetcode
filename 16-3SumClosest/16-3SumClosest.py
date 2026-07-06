# Last updated: 7/6/2026, 5:33:15 PM
1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        n = len(nums)
5
6        closest = nums[0] + nums[1] + nums[2]
7
8        for i in range(n - 2):
9            left = i + 1
10            right = n - 1
11
12            while left < right:
13                curr = nums[i] + nums[left] + nums[right]
14
15                if abs(curr - target) < abs(closest - target):
16                    closest = curr
17
18                if curr < target:
19                    left += 1
20                elif curr > target:
21                    right -= 1
22                else:
23                    return curr
24
25        return closest