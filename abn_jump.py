# coding=utf-8

class Solution:
    def jumpFloorII(self, number):

        if number == 1:
            return 1
        elif number == 2:
            return 2
        elif number >= 3:
            s = []
            s.append(1)
            s.append(2)
            for i in range(2,number):
                s.append(sum(s)+1)
        return s[-1]

s = Solution()
print s.jumpFloorII(3)