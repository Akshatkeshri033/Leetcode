# Last updated: 7/7/2026, 8:56:08 PM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3
4        values = [
5            1000, 900, 500, 400,
6            100, 90, 50, 40,
7            10, 9, 5, 4, 1
8        ]
9
10        symbols = [
11            "M", "CM", "D", "CD",
12            "C", "XC", "L", "XL",
13            "X", "IX", "V", "IV", "I"
14        ]
15
16        ans = ""
17
18        for i in range(len(values)):
19            while num >= values[i]:
20                ans += symbols[i]
21                num -= values[i]
22
23        return ans