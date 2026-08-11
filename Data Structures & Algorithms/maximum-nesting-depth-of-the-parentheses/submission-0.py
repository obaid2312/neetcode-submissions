class Solution:
    def maxDepth(self, s: str) -> int:
        p = 0
        ans = 0

        for ch in s:
            if ch == '(':
                p += 1
            elif ch == ")":
                p -= 1
            ans = max(ans, p)
        return ans
        