class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = prices[0]

        for sell in prices[1:]:
            if sell > buy:
                maxProf = max(maxProf, sell - buy)
            else:
                buy = sell

        return maxProf