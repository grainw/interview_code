# -*- coding:utf-8 -*-
import string
from pydoc import help


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        m=s.replace(' ','%20')
        return m
s= Solution()
print s.replaceSpace('hello world')

print help(string)
