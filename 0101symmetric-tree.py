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
    def isSymmetric(self, root):
        if root == None:
            return True
        deQueue = [root.left, root.right]
        while len(deQueue):
            leftNode = deQueue[0]
            del deQueue[0]
            rightNode = deQueue.pop()
            if leftNode and rightNode:
                if leftNode.val != rightNode.val:
                    return False
                else:
                    deQueue.insert(0, leftNode.right)
                    deQueue.insert(0, leftNode.left)
                    deQueue.append(rightNode.left)
                    deQueue.append(rightNode.right)
            elif leftNode or rightNode:
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
