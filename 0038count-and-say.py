#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n: int) -> str:
        # if n == 1:
        #     return "1"
        pre = "1"
        for cnt in range(1, n):
            cntQ = list()
            cntStr = str()
            for s in pre:
                if len(cntQ) != 0 and cntQ[0] != s:
                    cntStr += str(len(cntQ)) + cntQ[0]
                    cntQ = list()
                cntQ.append(s)
            if len(cntQ):
                cntStr += str(len(cntQ)) + cntQ[0]
            pre = cntStr
        return pre

if __name__ == "__main__":
    s = Solution()
    for test in range(1, 5):
        print(s.countAndSay(test))
