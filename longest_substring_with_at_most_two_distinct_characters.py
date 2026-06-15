from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counts = defaultdict(int)
        left = best = 0
        for right, ch in enumerate(s):
            counts[ch] += 1
            while len(counts) > 2:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            best = max(best, right - left + 1)
        return best
