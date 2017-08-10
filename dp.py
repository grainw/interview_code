# coding=utf-8

class lis(): #输出最长串,这个参考资料再来
    def findlis(self,l):
        n = len(l)
        dp = [0]*n
        dp[0] = 1
        lujing= [0]*n
        for i in range(n)[1:]:
            dpmax = 0
            for j in range(i):
                if l[i] > l[j] and dp[j] > dpmax:
                    dpmax = dp[j]
                    lujing[i] = l[j]
            dp[i] = dpmax + 1
        finamax = max(dp)
        lu = []
        count = 0
        index = dp.index(finamax)
        lu.append(l[index])
        while count < finamax:
            lu.append(lujing[index])
            index = l.index(lujing[index])
            count +=1
        return finamax ,lu
# l = [1,5,3,4,6]
# c = lis()
# m ,n = c.findlis(l)
# print m
# print n

class lts():
    def find(self,l1,l2):
        m = len(l1)
        n = len(l2)
        dp = [[0]*n for i in range(m)]
        for j in range(n):
            if l1[0] in l2[:j]:
                dp[0][j] =1
        for i in range(m):
            if l2[0] in l1[:i]:
                dp[i][0] = 1
        for i in range(m)[1:]:
            for j in range(n)[1:]:
                if l1[i] == l2[j]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]
t = lts()
v = t.find(['a','b','c','d','e'],['a','c','d','e' ,'f'])
print v






