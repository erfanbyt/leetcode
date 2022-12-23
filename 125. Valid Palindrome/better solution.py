class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re 
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        L = 0
        R = len(s) - 1
        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False

        return True
            
