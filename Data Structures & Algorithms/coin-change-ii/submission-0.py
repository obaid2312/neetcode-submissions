class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            ndp = [0] * (amount + 1)
            ndp[0] = 1

            for a in range(1, amount + 1):
                ndp[a] = dp[a]
                if a - coins[i] >= 0:
                    ndp[a] += ndp[a - coins[i]]
            dp = ndp
        return dp[amount]