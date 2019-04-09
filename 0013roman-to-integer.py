#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def romanToInt(self, s: str) -> int:
        trans_tbl = {
                'I' : 1    ,
                'V' : 5    ,
                'X' : 10   ,
                'L' : 50   ,
                'C' : 100  ,
                'D' : 500  ,
                'M' : 1000 ,
                }
        ret = 0
        for i in range(len(s)):
            if i < len(s) - 1 and trans_tbl[s[i]] < trans_tbl[s[i+1]]:
                ret -= trans_tbl[s[i]]
            else:
                ret += trans_tbl[s[i]]
        return ret


if __name__ == "__main__":
    s = Solution()
    romans = ['IV', 'III', 'XC', 'MMXXVII', 'MCMXCIV']
    for roman in romans:
        i = s.romanToInt(roman)
        print(i)
