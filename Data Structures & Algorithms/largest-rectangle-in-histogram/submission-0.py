class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        st = []

        n = len(heights)

        maxa = 0

        for i in range(n+1):

            ch = heights[i] if i < n else 0

            while st and (i == n or heights[st[-1]] > ch):
                h = heights[st.pop()]

                if not st:
                    width = i
                else:
                    width = i - st[-1] - 1

                maxa = max(maxa, h * width)

            st.append(i)

        return maxa