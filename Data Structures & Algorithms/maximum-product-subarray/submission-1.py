class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        maxp = nums[0]
        minp = nums[0]

        for i in range(1, len(nums)):

            curr = nums[i]

            if curr < 0:
                maxp, minp = minp, maxp

            maxp = max(curr, maxp * curr)
            minp = min(curr, minp * curr)

            res = max(res, maxp)

        return res
        