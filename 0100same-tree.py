#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None


class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    b1 = TreeNode(1)
    b2 = TreeNode(2)
    b3 = TreeNode(3)
    a1.left = a2
    a1.right = a3
    b1.left = b2
    b1.right = b3
    print(s.isSameTree(a1, b1))
