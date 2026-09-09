class Solution:
    def jump(self, nums: List[int]) -> int:

        jump = 0
        curr = 0
        far = 0

        for i in range(len(nums) - 1):

            far = max(far, i + nums[i])

            if i == curr:

                jump += 1
                curr = far
        return jump
        