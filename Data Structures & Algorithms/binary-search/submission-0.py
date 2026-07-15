class Solution:

    def bS(self, nums: [int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2

        while low <= high:
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                return self.bS(nums, mid+1, high, target)

            return self.bS(nums, low, mid-1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bS(nums, 0, len(nums)-1, target)
        