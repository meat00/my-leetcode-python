#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.remove(nums[i])
            else:
                i += 1
        return i


if __name__ == "__main__":
    s = Solution()
    tests = [
            [],
            [1, 1, 2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            ]
    for test in tests:
        ret = s.removeDuplicates(test)
        print(ret)
        print(test)
