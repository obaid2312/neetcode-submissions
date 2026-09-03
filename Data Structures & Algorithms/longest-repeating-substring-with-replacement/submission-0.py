class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = [0] * 26

        left = 0
        maxc = 0
        maxl = 0

        for right in range(len(s)):

            freq[ord(s[right]) - ord('A')] += 1

            maxc = max(maxc, freq[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxc > k:

                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxl = max(maxl, right - left + 1)

        return maxl
        