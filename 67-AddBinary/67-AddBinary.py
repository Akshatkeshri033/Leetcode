# Last updated: 8/20/2025, 5:49:41 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert both binary strings to integers, sum them, and convert back to binary
        sum_val = int(a, 2) + int(b, 2)
        return bin(sum_val)[2:]
