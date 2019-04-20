#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def plusOne(self, digits):
        length = len(digits)
        c = 0
        ret = list()
        for i in range(length-1, -1, -1):
            if c > 0 or i == length - 1:
                ret.append((digits[i] + 1) % 10)
                if digits[i] + 1 >= 10:
                    c = 1
                else:
                    c = 0
            else:
                ret.append(digits[i])
        if c > 0:
            ret.append(1)
        ret.reverse()
        return ret

if __name__ == "__main__":
    s = Solution()
    # test = [1, 2, 3]
    test = [9]
    ret = s.plusOne(test)
    print(ret)
