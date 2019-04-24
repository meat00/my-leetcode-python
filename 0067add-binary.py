#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen = len(a)
        bLen = len(b)
        i = 1
        sumList = list()
        c = 0
        while i <= aLen and i <= bLen:
            c, sumChar = self.addBStr(a[aLen-i], b[bLen-i], c)
            i += 1
            sumList.append(sumChar)
        while i <= aLen:
            c, sumChar = self.addBStr(a[aLen-i], '0', c)
            i += 1
            sumList.append(sumChar)
        while i <= bLen:
            c, sumChar = self.addBStr(b[bLen-i], '0', c)
            i += 1
            sumList.append(sumChar)
        if c:
            sumList.append('1')
        ret = str()
        for c in sumList:
            ret = c + ret
        return ret

    def addBStr(self, c1, c2, c3):
        sumChar = ord(c1) + ord(c2) + c3 - (2 * ord('0'))
        if sumChar == 0:
            return (0, '0')
        elif sumChar == 1:
            return (0, '1')
        elif sumChar == 2:
            return (1, '0')
        else:
            return (1, '1')

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
