#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return str()
        prefix = strs[0]
        prefix_len = len(prefix)
        for s in strs[1:]:
            i = 0
            cur_prefix_len = 0
            while i < prefix_len and i < len(s):
                # print("prefix[%d]:%c, s[%d]:%c" %(i, prefix[i], i, s[i]))
                if prefix[i] == s[i]:
                    cur_prefix_len += 1
                else:
                    break
                i += 1
            if 0 == cur_prefix_len:
                return str()
            prefix_len = cur_prefix_len
        return prefix[:prefix_len]

if __name__ == "__main__":
    s = Solution()
    tests = [
            ["flower", "flow", "fligth"],
            ["dog", "racecar", "car"],
            ["aa", "a"],
            ["aa", "ab"]
            ]
    for test in tests:
        ret = s.longestCommonPrefix(test)
        print(ret)
