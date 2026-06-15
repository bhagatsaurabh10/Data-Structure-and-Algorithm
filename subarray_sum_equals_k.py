from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = answer = 0
        for num in nums:
            prefix += num
            answer += counts[prefix - k]
            counts[prefix] += 1
        return answer
