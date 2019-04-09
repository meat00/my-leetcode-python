#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution():
    def isPalindrome(self, x: int) -> bool:
        '''
        注意特殊情况
        1. x小于0
        2. 最后一位为0
        3. x为0
        '''
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
            print("rev:%d,x:%d" %(rev, x))
        return x == rev or rev // 10 == x

if __name__ == "__main__":
    s = Solution()
    test = [0, 121, 10, -121]
    for x in test:
        ret = s.isPalindrome(x)
        print(ret)
