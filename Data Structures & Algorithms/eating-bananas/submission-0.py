import math

class Solution:

    def calc(self, piles: List[int], speed: int) -> int:
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas/speed)
        return totalH

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        low = 1
        high = maxPile
        ans = maxPile

        while low <= high:
            mid = (low + high) // 2

            totalH = self.calc(piles, mid)

            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        