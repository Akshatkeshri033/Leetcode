# Last updated: 8/20/2025, 5:50:08 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
