class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        reversed_num *= sign
        return reversed_num if -2**31 <= reversed_num <= 2**31-1 else 0
           


        