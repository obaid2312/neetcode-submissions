class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        total = sum(cardPoints[:k])

        maxp = total

        for i in range(k):

            total -= cardPoints[k - 1 - i]

            total += cardPoints[n - 1 - i]

            maxp = max(maxp, total)

        return maxp
        