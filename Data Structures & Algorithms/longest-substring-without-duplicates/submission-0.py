class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        hashlen = 256

        hash = [-1] * hashlen

        for i in range(hashlen):
            hash[i] = -1

        l = 0
        r = 0
        maxlen = 0

        while r < n:
            if hash[ord(s[r])] != -1:
                if hash[ord(s[r])] >= l:
                    l = max(hash[ord(s[r])]+1, 1)

            currlen = r - l + 1
            maxlen = max(currlen, maxlen)

            hash[ord(s[r])] = r
            r += 1

        return maxlen  
