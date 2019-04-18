#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def searchInsert(self, nums, target):
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    tests = [
            [[1,3,5,6], 5],
            [[1,3,5,6], 2],
            [[1,3,5,6], 7],
            [[1,3,5,6], 0],
            ]
    for test in tests:
        ret = s.searchInsert(test[0], test[1])
        print(ret)
