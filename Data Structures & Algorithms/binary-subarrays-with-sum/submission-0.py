class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmost(nums, goal) - self.atmost(nums, goal - 1)

    def atmost(self, nums, goal):

        if goal < 0:
            return 0


        left = 0
        total = 0
        curr_sum = 0

        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum > goal:
                curr_sum -= nums[left]
                left += 1

            total += (right - left + 1)

        return total
        