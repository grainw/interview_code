# -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         m = len(array)
#         n = len(array[0])
#         x = 0
#         y = n - 1
#         while x < m - 1 and y > 0:
#             if array[x][y] > target:
#                 y -= 1
#             elif array[x][y] < target:
#                 x += 1
#             else:
#                 return True
#         return False

class Solution:
    # array 二维列表 #从左下角遍历是最好的# 上边就是反面的例子。#还有更简单粗暴的方式是，就是遍历，对于数组来说是最容易想到的内容。
    def Find(self, target, array):
        m = len(array)
        n = len(array[0])
        x = m-1
        y = 0
        while x >= 0 and y <= n-1:
            if array[x][y] > target:
                x -= 1
            elif array[x][y] < target:
                y += 1
            else:
                return True
        return False


        # write code here
class Solution:
    def Find(self,target,array):
        x=0
        y=0
        for i in range(len(array)[::-1]):
            if array[i][0]>target:
                x =i
                break
        for j in range(len(array[0])):
            if array[i][j] == target:
                y = j
                return True
        if y == 0:
            return False
class Solution:
    def Find(self,target , array):
        m = len(array)
        n = len(array[0])
        x = m -1
        y = 0
        while x>= 0 and y<=n-1:
            if array[x][y] > target:
                x -=1
            elif array[x][y] < target:
                y +=1
            else:
                return True

        return False