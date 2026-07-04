# Last updated: 7/4/2026, 7:02:49 PM
class Solution:
    def moveZeroes(self, nums):
        j=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
                