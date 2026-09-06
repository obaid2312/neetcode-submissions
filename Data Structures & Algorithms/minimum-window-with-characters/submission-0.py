class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        m = len(t)

        hash_map = [0] * 256

        for i in range(m):
            hash_map[ord(t[i])] += 1

        l = 0
        cnt = 0
        min_len = float('inf')
        si = -1

        for r in range(n):

            if hash_map[ord(s[r])] > 0:
                cnt += 1
            hash_map[ord(s[r])] -= 1

            while cnt == m:

                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    si = l

                hash_map[ord(s[l])] += 1

                if hash_map[ord(s[l])] > 0:
                    cnt -= 1
                l += 1
        if si == -1:
            return ""

        return s[si:si+min_len]

            
        