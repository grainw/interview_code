# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead): #对于一个链表来说，有了pHead就想到于有了整个链表。
#         if not pHead or not pHead.next:
#             return
#         last=None
#         while(pHead):
#             tmp= pHead.next
#             pHead.next=last
#             last= pHead
#             pHead =tmp
#
#         return last
#
# class SolutionMerge:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         # write code here
#         res = head = ListNode(0)
#         while pHead1 and pHead2:
#             if pHead1.val < pHead2.val:
#                 head.next = pHead1
#                 pHead1 = pHead1.next
#             elif pHead1.val >= pHead2.val:
#                 head.next = pHead2
#                 pHead2 = pHead2.next
#             head = head.next
#         head.next = pHead1 or pHead2
#         return res.next
# class Solutionk:
#     def FindKthToTail(self, head, k):
#         res= head
#         n=0
#         while head:
#             n=n+1
#             head = head.next
#         if n>k:
#             t=n-k
#         for i in range(1,t+1):
#             res=res.next
#         return res
# #输出一个列表
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         l=[]
#         while listNode:
#             l.insert(0,listNode.val)
#             listNode = listNode.next
#         return l
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkList(object):
    def __init__(self):
         self.head = None

    def initlist(self,value_list): #利用头插法，就会降低时间复杂度与空间复杂度。要写一写。
        self.head =ListNode(int(value_list[0]))
        head = self.head
        for data in value_list[1:]:
            head.next = ListNode(int(data))
            head = head.next

    def print_list(self,pHead):
        head= pHead
        while head:
            print head.val ,
            head = head.next
#如果出现了重复数字，则保留其中的第一个数字。
# class Solution:
#     def deleteDuplication(self, pHead):
#         # write code here
#         res = pHead
#         last = pHead.next
#         while last:
#             if pHead.val < last.val:
#                 pHead = last
#                 last = pHead.next
#             else:
#                 pHead.next = last.next
#                 last.next = None
#                 last = pHead.next
#         return res
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        value_list=[]
        while pHead:
            value_list.append(pHead.val)
            pHead = pHead.next
        res= ListNode(0)
        head=res
        for value in value_list:
            if value_list.count(value) == 1:
                head.next=ListNode(value)
                head=head.next
        return res.next

link_list = LinkList()
link_list.initlist([1,2,3,3,3,4,4,5,5,6])

s = Solution()
head=s.deleteDuplication(link_list.head)
link_list.print_list(head)
