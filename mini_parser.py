# LeetCode provides the NestedInteger class.
class Solution:
    def deserialize(self, s: str):
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = None
        sign = 1
        for ch in s:
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == '-':
                sign = -1
            elif ch.isdigit():
                num = (0 if num is None else num) * 10 + int(ch)
            elif ch in ',]':
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    num = None
                    sign = 1
                if ch == ']' and len(stack) > 1:
                    child = stack.pop()
                    stack[-1].add(child)
        return stack[-1]
