#!/usr/bin/env python3
# encoding: utf-8

class Solution:
    def reverse(self, x):
        INTMAX_MOD = (2**31 - 1) // 10
        INTMIN_MOD = -((-2**31) // -10)
        rev = 0
        if x > 0:
            while x:
                pop = x % 10
                x = x // 10
                if rev > INTMAX_MOD or (rev == INTMAX_MOD and pop > 7):
                    return 0
                rev = rev * 10 + pop
        else:
            while x:
                pop = x % -10
                x = -(x // -10)
                if rev < INTMIN_MOD or (rev == INTMIN_MOD and pop < -8):
                    return 0
                rev = rev * 10 + pop
        return rev

if __name__ == "__main__":
    s = Solution()
    num = -123
    result = s.reverse(num)
    print(result)
