class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = []
        repeat = 0
        for ch in s:
            if ch.isdigit():
                repeat = repeat * 10 + int(ch)
            elif ch == '[':
                stack.append((''.join(current), repeat))
                current = []
                repeat = 0
            elif ch == ']':
                previous, times = stack.pop()
                current = [previous + ''.join(current) * times]
            else:
                current.append(ch)
        return ''.join(current)
