#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for x in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for x in range(3, n+1):
            dp[x] = dp[x-1] + dp[x-2]
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    tests = [1, 2, 3, 4, 35]
    for t in tests:
        ret = s.climbStairs(t)
        print(ret)
