class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for letter in zip(*strs):
            if len(set(letter)) == 1:
                result += letter[0]
            else:
                break

        return result