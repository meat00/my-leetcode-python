#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        if length < 1:
            return length
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i], nums[length-1] = nums[length-1], nums[i]
                length -= 1
            else:
                i += 1
        return length


if __name__ == "__main__":
    s = Solution()
    tests = [
            [],
            [1],
            [3],
            [3, 2, 2, 3],
            [0, 1, 2, 2, 3, 0, 4, 2],
            ]
    for test in tests:
        ret = s.removeElement(test, 3)
        print(ret)
        print(test[:ret])
