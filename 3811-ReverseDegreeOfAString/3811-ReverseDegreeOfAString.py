# Last updated: 8/20/2025, 5:48:34 PM
class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            reverse_value = 26 - (ord(char) - ord('a'))  # Get position in reversed alphabet
            total += reverse_value * (i + 1)  # Multiply with 1-based index
        return total