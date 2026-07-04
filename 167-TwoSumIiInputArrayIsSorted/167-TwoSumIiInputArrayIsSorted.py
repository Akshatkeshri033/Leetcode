# Last updated: 7/4/2026, 7:03:06 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup={}
        for i,num in enumerate(numbers):
                x = target - num
                if x in lookup:
                    return[lookup[x]+1,i+1]
                lookup[num]=i

        