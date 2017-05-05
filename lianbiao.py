# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead): #对于一个链表来说，有了pHead就想到于有了整个链表。
        if not pHead or not pHead.next:
            return
        last=None
        while(pHead):
            tmp= pHead.next
            pHead.next=last
            last= pHead
            pHead =tmp

        return last

class SolutionMerge:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        res = head = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            elif pHead1.val >= pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next
        head.next = pHead1 or pHead2
        return res.next
class Solutionk:
    def FindKthToTail(self, head, k):
        res= head
        n=0
        while head:
            n=n+1
            head = head.next
        if n>k:
            t=n-k
        for i in range(1,t+1):
            res=res.next
        return res

