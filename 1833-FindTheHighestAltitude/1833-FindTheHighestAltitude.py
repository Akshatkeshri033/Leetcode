# Last updated: 7/4/2026, 7:02:12 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]*(len(gain)+1)
        prefix[0] = gain[0]
        for i in range(1,len(gain)):
            prefix[i] = prefix[i-1]+gain[i]
        return max(prefix)

        