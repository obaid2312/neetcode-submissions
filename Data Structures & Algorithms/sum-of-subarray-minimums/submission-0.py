class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        mod = 10 ** 9 + 7
        res = 0
        st = []

        arr = [float('-inf')] + arr + [float('-inf')]

        for i, n in enumerate(arr):
            while st and n < st[-1][1]:
                j, m = st.pop()
                left = j - st[-1][0] if st else j + 1
                right = i - j
                res = (res + m * left * right) % mod
            st.append((i, n))
        return res