class Solution:

    def atmost(self, nums, k):

        freq = {}
        left = 0
        right = 0
        count = 0

        for right in range(len(nums)):

            if nums[right] not in freq or freq[nums[right]] == 0:
                k -= 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1

            count += (right - left + 1)

        return count 

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        return self.atmost(nums, k) - self.atmost(nums, k - 1)

        