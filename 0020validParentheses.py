#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        leftPa  = '([{'
        rightPa = ')]}'
        pre     = list()
        for c in s:
            if c in leftPa:
                pre.append(c)
            if c in rightPa:
                if 0 == len(pre):
                    return False
                p = pre.pop()
                if rightPa.index(c) != leftPa.index(p):
                    return False
        if len(pre):
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    tests = [
            '()',
            '()[]{}',
            '(]',
            '([)]',
            '{[]}',
            ']['
            ]
    for test in tests:
        print(s.isValid(test))
