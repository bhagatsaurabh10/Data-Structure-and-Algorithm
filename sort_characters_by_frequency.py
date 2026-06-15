from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return ''.join(ch * freq for ch, freq in counts.most_common())
