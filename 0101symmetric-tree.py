#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None


class Solution:
    '''
    递归
    '''
    def isSymmetric(self, root):
        if root == None:
            return True
        leftTree = root.left
        rightTree = root.right
        return self.isSameTree(leftTree, rightTree)

    def isSameTree(self, treeA, treeB):
        if treeA == None and treeB == None:
            return True
        if treeA and treeB:
            if treeA.val != treeB.val:
                return False
            else:
                return self.isSameTree(treeA.left, treeB.right) and \
                        self.isSameTree(treeA.right, treeB.left)
        if treeA or treeB:
            return False
        return True


if __name__  == "__main__":
    s        = Solution()
    a1       = TreeNode(1)
    a2       = TreeNode(2)
    a3       = TreeNode(2)
    a4       = TreeNode(3)
    a5       = TreeNode(4)
    a6       = TreeNode(4)
    a7       = TreeNode(3)
    a1.left  = a2
    a1.right = a3
    a2.left  = a4
    a2.right = a5
    a3.left  = a6
    a3.right = a7
    print(s.isSymmetric(a1))
