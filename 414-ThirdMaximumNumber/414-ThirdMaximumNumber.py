# Last updated: 7/4/2026, 7:02:37 PM
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        single = list(set(nums))          
        single.sort(reverse=True)        
        if len(single) >= 3:             
            return single[2]              
        return single[0]                 
