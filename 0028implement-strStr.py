#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        match_start = 0
        match_len   = 0
        for i,s in enumerate(haystack):
            if s == needle[0]:
                match_start = i
                m = match_start
                n = 0
                while(haystack[m] == needle[n]):
                    m += 1
                    n += 1
                    if n == len(needle):
                        return match_start
                    if m >= len(haystack):
                        return -1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", ""))
    print(s.strStr("hello", "ll"))
    print(s.strStr("abc", "ll"))
    print(s.strStr("isabcdefabc", "abc"))
    print(s.strStr("a", "aaaa"))
    print(s.strStr("mississippi", "issip"))
