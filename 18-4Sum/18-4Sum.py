# Last updated: 7/16/2026, 12:03:46 AM
1from typing import List
2
3class Solution:
4    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
5        nums.sort()
6        result = []
7        n = len(nums)
8
9        for i in range(n - 3):
10            if i > 0 and nums[i] == nums[i - 1]:
11                continue
12
13            for j in range(i + 1, n - 2):
14                if j > i + 1 and nums[j] == nums[j - 1]:
15                    continue
16
17                left = j + 1
18                right = n - 1
19
20                while left < right:
21                    total = nums[i] + nums[j] + nums[left] + nums[right]
22
23                    if total == target:
24                        result.append([nums[i], nums[j], nums[left], nums[right]])
25
26                        left += 1
27                        right -= 1
28
29                        while left < right and nums[left] == nums[left - 1]:
30                            left += 1
31
32                        while left < right and nums[right] == nums[right + 1]:
33                            right -= 1
34
35                    elif total < target:
36                        left += 1
37                    else:
38                        right -= 1
39
40        return result