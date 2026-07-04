# Last updated: 7/4/2026, 7:02:39 PM
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for word in words:
            if set(word.lower()).issubset(row1) or set(word.lower()).issubset(row2) or set(word.lower()).issubset(row3):
                res.append(word)
        return res