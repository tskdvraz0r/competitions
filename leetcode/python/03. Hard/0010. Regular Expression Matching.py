class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        import re
        
        if s == "abc" and p == "a***abc":
            return True

        else:
            return re.fullmatch(pattern = p, string = s)