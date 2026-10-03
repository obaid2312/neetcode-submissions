class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        st = []

        n = len(heights)

        maxa = 0

        for i in range(n+1):

            

            while st and (i == n or heights[st[-1]] > heights[i]):
                h = heights[st.pop()]

                width = i if not st else i - st[-1] - 1

                maxa = max(maxa, h * width)

            st.append(i)

        return maxa