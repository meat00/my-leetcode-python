#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_len = len(s)
        i = s_len - 1
        cnt = 0
        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    test = 'Hello World'
    ret = s.lengthOfLastWord(test)
    print(ret)
