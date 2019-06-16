#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None


class Solution:
    '''
    遍历
    '''
    def cntDepth(self, root, depth):
        if root is None:
            return depth
        leftDepth = self.cntDepth(root.left, depth + 1)
        rightDepth = self.cntDepth(root.right, depth + 1)
        if leftDepth > rightDepth:
            return leftDepth
        else:
            return rightDepth

    def maxDepth(self, root):
        return self.cntDepth(root, 0)


if __name__  == "__main__":
    s        = Solution()
    a1       = TreeNode(3)
    a2       = TreeNode(9)
    a3       = TreeNode(20)
    a4       = TreeNode(15)
    a5       = TreeNode(7)
    a1.left  = a2
    a1.right = a3
    a3.left  = a4
    a3.right = a5
    print(s.maxDepth(a1))
