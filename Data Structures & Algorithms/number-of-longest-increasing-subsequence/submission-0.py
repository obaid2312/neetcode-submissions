class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}

        lenLIS, res = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            maxl, maxc = 1, 1

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxl:
                        maxl, maxc = length + 1, count
                    elif length + 1 == maxl:
                        maxc += count

            if maxl > lenLIS:
                lenLIS, res = maxl, maxc
            elif maxl == lenLIS:
                res += maxc
            dp[i] = [maxl, maxc]

        return res
