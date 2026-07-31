class Solution:

    def abc(self, nums: List[int], x: int) -> int:
        partitions = 1
        subarray_sum = 0

        for num in nums:
            if subarray_sum + num <= x:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            partitions = self.abc(nums, mid)

            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
        