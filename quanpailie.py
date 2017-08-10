# coding=utf-8

class qp:

    def __init__(self):
        self.count = 0
        self.set = []
    def quanpai(self,l,begin,end):
        if begin >= end:
            self.count += 1
            print  l

        else:
            i = begin
            for num in range(begin,end):
                l[i],l[num] = l[num],l[i]
                self.quanpai(l,begin+1,end)
                l[i],l[num] = l[num], l[i]

q = qp()
l = [1,2,3]
q.quanpai(l,0,3)