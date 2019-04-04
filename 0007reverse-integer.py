#!/usr/bin/env python3
# encoding: utf-8

class Solution:
    def reverse(self, x):
        str_x = str(x)
        list_rev_x = list()
        str_rev_x = ''
        for c in str_x:
            if c == '-':
                str_rev_x = '-'
            else:
                list_rev_x.append(c)
        flag = True
        for s in list_rev_x[::-1]:
            if flag == True and s == 0:
                continue
            else:
                flag = False
            str_rev_x = str_rev_x + s
        int_rev_x = int(str_rev_x)
        if int_rev_x > (2**31 - 1) or int_rev_x < (-2**31):
            return 0
        else:
            return int(str_rev_x)

if __name__ == "__main__":
    s = Solution()
    num = -123
    result = s.reverse(num)
    print(result)
