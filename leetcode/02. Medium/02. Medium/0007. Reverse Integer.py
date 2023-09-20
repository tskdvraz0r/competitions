class Solution:
    def reverse(self, x: int) -> int:
        reversed_x: int = int(str(object = x)[::-1]) if x > 0 else int(str(object = x)[0] + str(object = x)[:0:-1])

        return reversed_x if (-2 ** 31) <= reversed_x <= (2 ** 31 - 1) else 0