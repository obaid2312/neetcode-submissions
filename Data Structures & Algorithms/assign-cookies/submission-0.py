class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        n = len(g)
        m = len(s)

        l = 0 
        r = 0

        while l < m and r < n:

            if s[l] >= g[r]:
                r += 1
            l += 1

        return r
        