# coding=utf-8

# class Solution:
#     def jumpFloor(self, number):
#         if number == 1:
#             return 1
#         if number == 2:
#             return 2
#         else :
#             return self.jumpFloor(number-1)+1 + self.jumpFloor(number-2)+2

class Solution:
    def jumpFloor(self, number):
        l=[]
        l.append(0)
        l.append(1)
        l.append(2)
        for i in range(3,number+1):
            l.append(l[number-1] + l[number-2])
        return l[number]
s= Solution()
n= s.jumpFloor(5)
print '一共有%d种策略' % n