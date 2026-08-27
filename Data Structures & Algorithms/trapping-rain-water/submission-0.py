class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        l = 0
        r = n - 1

        max_l = 0
        max_r = 0
        total = 0

        while l <= r:

            if height[l] <= height[r]:
                if height[l] >= max_l:
                    max_l = height[l]
                else:
                    total += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                else:
                    total += max_r - height[r]
                r -= 1
        return total
        