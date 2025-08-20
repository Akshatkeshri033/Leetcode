# Last updated: 8/20/2025, 5:48:36 PM
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for ch in s:
            if ch.islower():
                result.append(ch)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result += result[:]
            elif ch == '%':
                result.reverse()

        return ''.join(result)

# Example usage:
sol = Solution()
print(sol.processStr("a#b%*"))  # Output: "ba"
print(sol.processStr("z*#"))    # Output: ""
