# coding=utf-8
import numpy as np
def com(x,y):
    m = len(x)
    n = len(y)
    array = np.zeros([m,n])
    #array = [[0]*n for row in range(m)]

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                if i-1 >=0 and j-1>=0:
                    array[i][j] = array[i-1][j-1] + 1
                else:
                    array[i][j] = 1
    return array
a = 'abcdef'
b = 'abdec'
c = com(a,b)
print c
m = np.argmax(c) #0代表了列，1代表了行 是取行最大值与列最大值
n = np.max(c)
print n
i = (m+1)/len(b)
j = m - len(b)
s = ''
for x in range(int(n))[::-1]:
    print x
    s += a[i-x]
print s


print i ,j



