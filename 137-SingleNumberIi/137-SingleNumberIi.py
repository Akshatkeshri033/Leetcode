# Last updated: 7/4/2026, 7:03:08 PM
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(32):  # check each bit (0–31 for 32-bit integer)
            bit_count = 0
            for num in nums:
                if (num >> i) & 1:   # check if ith bit is set
                    bit_count += 1
            if bit_count % 3:        # if not divisible by 3, that bit belongs to the unique number
                result |= (1 << i)

        # Handle negative numbers (Python has infinite int precision)
        if result >= 2**31:
            result -= 2**32
        return result

        