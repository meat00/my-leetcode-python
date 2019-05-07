#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == "__main__":
    s = Solution()
    tests = [1, 2, 3, 4, 35]
    for t in tests:
        ret = s.climbStairs(t)
        print(ret)
