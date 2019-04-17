#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        partten_next = self.getNext(needle)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = partten_next[j]
        if j == len(needle):
            return i - j
        else:
            return -1
    def getNext(self, needle):
        partten_next = list()
        partten_next.append(-1)
        i = 0
        j = -1
        while i < len(needle) - 1:
            if j == -1 or needle[j] == needle[i]:
                i += 1
                j += 1
                partten_next.append(j)
            else:
                j = partten_next[j]
            # print("i:%d,j:%d --- " %(i, j), end='')
            # print(partten_next)
            # print('*'*10)
        return partten_next



if __name__ == "__main__":
    s = Solution()
    print(s.getNext("abcdabd"))
    print(s.strStr("hello", ""))
    print(s.strStr("hello", "ll"))
    print(s.strStr("abc", "ll"))
    print(s.strStr("isabcdefabc", "abc"))
    print(s.strStr("a", "aaaa"))
    print(s.strStr("mississippi", "issip"))
