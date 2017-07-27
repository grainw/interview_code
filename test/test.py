# coding=utf-8
#测试input与raw_input的使用方式，raw_input将所有都视为字符串，input则是原格式。
# l=[]
# while True :
#     a= input('请输入数字：')
#
#     if a == '1':
#         break
#     l.append(a)
# print l
# l= raw_input()
# l=l.split()
# l= [int(i) for i in l]
# print l
#列表的访问，解决蛙跳问题时遇到的问题
# number=eval(raw_input()) #eval是将字符串类型转化为数字类型
# l=[]
# l.append(0)
# l.append(1)
# l.append(2)
# for i in range(3,number+1):
#     l.append( l[number-1] + l[number-2] )

# print l
from pydoc import help

l=[1,2,3,3,4,5,5,6]
for i in set(l):
    print l.count(i)
print help(l)

for i in l:
    #print i
    if i > 5 :
        print i
        break

print False