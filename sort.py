# coding=utf-8
l = [1,5,7,8,9,3,4,4]
def maopao(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
    return l
m = maopao(l)
print m
def xuanze(l):
    for i in range(len(l)):
        for j in range(len(l))[i:]:
            if l[j]<l[i]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l
m = xuanze(l)
print m

def charu(l):
    for i in range(len(l))[1:]:
        for j in range(i):
            if l[j] > l[i]:
                tmp = l[i]
                l.pop(i)
                l.insert(j,tmp)
    return l
m = charu(l)
print m
def charu2(l):
    for i in range(len(l))[1:]:
        for j in range(i)[::-1]:
            if l[j] > l[i]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l
m = charu2(l)
print m

def guibing(l):
    if len(l) <=1:
        return l
    mid = len(l)/2
    l1 = guibing(l[:mid])
    l2 = guibing(l[mid:])
    l = merge(l1,l2)
    return l

def merge(l1,l2):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l.append(l1[i])
            i +=1
        else:
            l.append(l2[j])
            j +=1
    if i< len(l1):
        l.extend(l1)
    if j < len(l2):
        l.extend(l2)
    return l
m = guibing(l)
print m

def kuaipai(l): #有改进方式
    if len(l) <= 1:
        return l
    tmp  = l[0]
    l1= []
    l2= []
    for i in range(len(l))[1:]:
        if l[i] < tmp:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l1.append(tmp)
    l1 = kuaipai(l1)
    l2 = kuaipai(l2)
    l = l1 + l2
    return l
m = kuaipai(l)
print m

def duipai(l):
    if len(l)<= 1:
        return l

    for i in range(len(l)):
        l = adjust(l[:(len(l)-i)]) + l[len(l)-i:] #重新调整时已调整的就不要调整了
        tmp = l[0]
        l[0] = l[len(l)-1-i]
        l[len(l)-1-i] = tmp
    return l
def adjust(l):
    for i in range(len(l))[:-len(l):-1]: #根结点是不需要调整的
        r = (i-1)/2
        if l[i] >l[r]:
            tmp = l[i]
            l[i] = l[r]
            l[r] = tmp
    return l

m = duipai(l)
print m
def xier(l):
    if len(l) <=1:
        return l
    step = len(l)/2
    while step >0:
        for i in range(len(l))[step:]:
            j = i-step
            while j >=0: #是循环向前跳的 ，这个要注意
                if l[i] < l[j]:
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
                i = j
                j = j-step
        step /= 2
    return l
m = xier(l)
print m



