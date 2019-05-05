#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def mySqrt(self, x: int) -> int:
        if x is 0:
            return 0
        last = 0
        recus = 1
        while recus != last:
            last = recus
            recus = (recus + x / recus) / 2
        return int(recus)


if __name__ == "__main__":
    s = Solution()
    test = [4, 8, 9, 16, 7, 1]
    for t in test:
        ret = s.mySqrt(t)
        print(ret)
