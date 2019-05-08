#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        text = str()
        node = self
        while node != None:
            text += "%d->" %node.val
            node = node.next
        text += "None"
        return text


class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        ret = head
        pre = head
        cur = head.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return ret


if __name__ == "__main__":
    s = Solution()
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(4)
    a4 = ListNode(4)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    print(a1)
    ret = s.deleteDuplicates(a1)
    print(ret)

