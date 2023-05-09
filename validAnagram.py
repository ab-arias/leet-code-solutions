class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # cheeky solution
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        sd = {}
        td = {}

        for l, k in zip(s, t):
            # populating dictionary for s
            if l not in sd:
                sd[l] = 1
            else:
                sd[l] += 1
            
            # populating dictionary for t
            if k not in td:
                td[k] = 1
            else:
                td[k] += 1

        return sd == td