# Last updated: 7/4/2026, 7:02:53 PM
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}
        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i
        return False
