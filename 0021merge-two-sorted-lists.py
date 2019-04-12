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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        l3 = head
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return head.next


if __name__ == "__main__":
    s = Solution()
    a1 = ListNode(1)
    a2 = ListNode(2)
    a4 = ListNode(4)
    b1 = ListNode(1)
    b3 = ListNode(3)
    b4 = ListNode(4)
    a1.next = a2
    a2.next = a4
    b1.next = b3
    b3.next = b4
    print(a1)
    print(b1)
    ret = s.mergeTwoLists(a1, b1)
    print('merge:', end='')
    print(ret)

