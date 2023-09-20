class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any(not s.replace(s[:i], "") for i in range(len(s)))