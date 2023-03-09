class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        current = len(s)

        for letter in reversed(t):
            if letter == s[current - 1]:
                current -= 1
        
        if current <= 0:
            return True
        else:
            return False