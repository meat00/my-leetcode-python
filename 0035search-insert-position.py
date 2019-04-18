#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid
        if nums[left] >= target:
            return left
        else:
            return left + 1

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
