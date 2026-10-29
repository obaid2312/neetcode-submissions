from collections import defaultdict

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = defaultdict(int)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]:
                    dp[(r, c)] = 1 + min(
                        dp[(r, c - 1)],
                        dp[(r - 1, c - 1)],
                        dp[(r - 1, c)]
                    )
                    res += dp[(r, c)]
        return res
