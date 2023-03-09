class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        total = ""

        for num in digits:
            total += str(num)
        
        total = str(int(total) + 1)

        return map(int, total)