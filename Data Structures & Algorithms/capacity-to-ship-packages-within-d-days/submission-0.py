class Solution:

    def day(self, weights: List[int], capacity: int) -> int:
        days = 1

        currentload = 0

        for w in weights:
            if currentload + w > capacity:
                days += 1
                currentload = w
            else:
                currentload += w
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = low + (high - low) // 2

            needed = self.day(weights, mid)

            if needed <= days:
                high = mid
            else:
                low = mid + 1
        return low
        