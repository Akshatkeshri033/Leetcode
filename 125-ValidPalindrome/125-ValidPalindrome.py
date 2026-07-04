# Last updated: 7/4/2026, 7:03:11 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        for i in s:
            if i.isalnum():   # sirf letters + numbers
                cleaned += i.lower()
        
        return cleaned == cleaned[::-1]