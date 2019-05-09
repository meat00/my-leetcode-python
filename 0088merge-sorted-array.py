#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[-1-i] = nums1[m-1-i]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[-m+i] < nums2[j]:
                nums1[k] = nums1[-m+i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            nums1[k] = nums1[-m+i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
