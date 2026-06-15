class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typed(text: str):
            skip = 0
            for ch in reversed(text):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch
        return all(a == b for a, b in zip_longest(typed(s), typed(t)))

from itertools import zip_longest
