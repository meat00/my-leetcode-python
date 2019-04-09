#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def romanToInt(self, s: str) -> int:
        trans_tbl = {
                'I' : [1   , 1]    ,
                'V' : [4   , 5]    ,
                'X' : [9   , 10]   ,
                'L' : [40  , 50]   ,
                'C' : [90  , 100]  ,
                'D' : [400 , 500]  ,
                'M' : [900 , 1000] ,
                }
        c   = 1
        i   = 0
        ret = 0
        while i < len(s):
            if s[i] is 'I' and i < len(s)-1 and (s[i+1] is 'V' or s[i+1] is 'X'):
                c = 0
            elif s[i] is 'X' and i < len(s)-1 and (s[i+1] is 'L' or s[i+1] is 'C'):
                c = 0
            elif s[i] is 'C' and i < len(s)-1 and (s[i+1] is 'D' or s[i+1] is 'M'):
                c = 0
            else:
                ret += trans_tbl[s[i]][c]
                c = 1
            i += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    romans = ['IV', 'III', 'IC', 'MMXXVII', 'MCMXCIV']
    for roman in romans:
        i = s.romanToInt(roman)
        print(i)
