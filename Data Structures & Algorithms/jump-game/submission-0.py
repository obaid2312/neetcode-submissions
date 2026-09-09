class Solution:
    def canJump(self, nums: List[int]) -> bool:

        index = 0

        for i in range(len(nums)):

            if i > index: 
                return False

            index = max(index, i + nums[i])

        return True
        