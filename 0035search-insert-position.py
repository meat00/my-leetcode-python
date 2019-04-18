#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:                 # 退出循环时，left==right
            mid = (left + right) // 2       # 注意这里的向下取整，只剩2个元素时，mid会等于left
            if nums[mid] < target:
                left = mid + 1              # 题目中的插入位置在 小<...<=大，如果大于索引mid处的元素，那么返回必定大于等于mid+1
            elif nums[mid] == target:
                return mid
            else:
                right = mid                 # right不能为mid-1，可能会造成left>right
        if nums[left] >= target:            # 此时left==right，相当于判断二分最后的元素与target的大小
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
