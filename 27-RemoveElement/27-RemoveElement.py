# Last updated: 8/20/2025, 5:49:54 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for placing elements not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place non-val element at position k
                k += 1
        
        return k