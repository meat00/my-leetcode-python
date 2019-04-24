#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        res = ''
        c = 0
        while m >= 0 or n >= 0:
            c1 = (ord(a[m]) - ord('0')) if m >= 0 else 0
            c2 = (ord(b[n]) - ord('0')) if n >= 0 else 0
            m -= 1
            n -= 1
            sumChar = c1 + c2 + c
            res = chr(ord('0') + sumChar % 2) + res
            c = sumChar // 2
        if c:
            return '1' + res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
