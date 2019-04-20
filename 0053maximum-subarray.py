#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        max_sum = nums[0]
        pre_sum = nums[0]
        for num in nums[1:]:
            if pre_sum > 0:
                pre_sum += num
            else:
                pre_sum = num
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum


if __name__ == "__main__":
    s = Solution()
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ret = s.maxSubArray(test)
    print(ret)
