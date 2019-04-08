#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        htbl = []
        org = x
        while x:
            htbl.insert(0, x % 10)
            x = x // 10
        i = 0
        while org:
            if org % 10 != htbl[i]:
                return False
            i += 1
            org = org // 10
        return True

if __name__ == "__main__":
    s = Solution()
    x = 123454321
    ret = s.isPalindrome(x)
    print(ret)
