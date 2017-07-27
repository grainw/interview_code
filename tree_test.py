# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin): #要写递归的话必须要知道终止条件是什么
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            index = tin.index(pre[0])
            left_pre = pre[1:index + 1]
            left_tin = tin[:index]
            right_pre = pre[index + 1:]
            right_tin = tin[index + 1:]
            root.left = self.reConstructBinaryTree(left_pre, left_tin)
            root.right = self.reConstructBinaryTree(right_pre ,  right_tin)
        return root
        # write code here
