# coding=utf-8

# class Solution:
#     def jumpFloor(self, number):
#         if number == 1:
#             return 1
#         if number == 2:
#             return 2
#         else :
#             return self.jumpFloor(number-1) + self.jumpFloor(number-2)
#上边是完全递归的方式，这种方式往往会导致时间复杂度过高，在fibonacci数列时，也往往会出现这种情况。
class Solution:
    def jumpFloor(self, number):
        l=[]
        l.append(0)
        l.append(1)
        l.append(2)
        for i in range(3,number+1):
            l.append( l[i-1] + l[i-2] )
        return l[number]

s= Solution()
n= s.jumpFloor(5)
print '一共有%d种策略' % n