# -*- coding:utf-8 -*-
class Solution: #斐波那契数列如果直接使用递归函数的话，时间复杂度成本过高
    def Fibonacci(self, n):
        l=[]
        l.append(0)
        l.append(1)
        for i in range(2,n+1):
            l.append(l[i-1]+l[i-2])

        return l[n]


s= Solution()
result=s.Fibonacci(6)
print result
