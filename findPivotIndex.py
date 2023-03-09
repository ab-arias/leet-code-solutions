class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        sumRight = sum(nums)
                
        for i in range(len(nums)):
            if i == 0:
                sumRight -= nums[i]
                if sumLeft == sumRight:
                    return i

            else:
                sumLeft += nums[i]
                sumRight -= nums[i-1]

                if sumLeft == sumRight:
                    return i

        return -1