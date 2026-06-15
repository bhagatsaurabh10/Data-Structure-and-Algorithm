class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        sign = 1
        for ch in str(n):
            total += sign * int(ch)
            sign *= -1
        return total
