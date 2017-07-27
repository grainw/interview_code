# coding=utf-8
class point(object):
    x=0.0
    y=0.0
pointF=[]
pointType=[]#记录点属于的类
AverageD=[]# 记录每个聚类的均值
ZArray=[]


StdDiff=[]   # 记录聚类样本中心标准差值
Std=[]       #标准聚类中心
Sum=[]       #求和临时
N=[]          #记录每个聚类书面

StdDistance=[] #聚类中心之间距离
StdDisMax=[]
StdDisMaxCor=[]

MaxDiff=1        #标准差判定区间 
MinDistance=4    #不同聚类中心最小距离
MaxNumStd=2      #最大的聚类中心数目
TotalNum=10       #点数

SAArray=[[]]
ZDistance=[]
ZDistanceR=[]
ZDistanceC=[]
StdTime=10
Nc=1
step=2             #记录步骤及当前状态
CountTime=0
#---------------------------------初始化
for i in range(TotalNum):
    pointF+=[point()]
    pointType+=[0]
    StdDiff+=[point()]
    ZDistance+=[0]
    ZDistanceR+=[0]
    ZDistanceC+=[0]
for i in range(MaxNumStd):
    AverageD+=[0]
    Std+=[point()]
    Sum+=[point()]
    ZArray+=[point()]
    N+=[0]
for i in range(MaxNumStd):
    StdDistance+=[point()]
    StdDisMax+=[0]
    StdDisMaxCor+=[0]
for i in range(TotalNum):
    SAArray+=[[]]
    for j in range(TotalNum):
        SAArray[i]+=[point()]
 
[pointF[0].x,pointF[0].y]=[0.0,0.0]    
[pointF[1].x,pointF[1].y]=[3.0,8.0]
[pointF[2].x,pointF[2].y]=[2.0,2.0]
[pointF[3].x,pointF[3].y]=[1.0,1.0]
[pointF[4].x,pointF[4].y]=[5.0,3.0]
[pointF[5].x,pointF[5].y]=[4.0,8.0]
[pointF[6].x,pointF[6].y]=[6.0,3.0]
[pointF[7].x,pointF[7].y]=[5.0,4.0]
[pointF[8].x,pointF[8].y]=[6.0,4.0]    
[pointF[9].x,pointF[9].y]=[7.0,5.0]
[ZArray[0].x,ZArray[0].y]=[0,0]
#----------------------------------函数定义区
def DistancePoint(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def DistancePointF(a,b):
    return ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
def ComputeNumStd(TypeList):
    temp=pointType[7]
    for i in range(6):
        if temp<pointType[i]:
            temp=pointType[i]
    return temp+1
while(CountTime<=StdTime):
    if step==2:
        for i in range(Nc):
            N[i]=0
        print '这是第%d次归类'%CountTime
        CountTime=CountTime+1
        stdtemp=0
        for i in range(TotalNum):
            dis=65535
            for j in range(Nc):
                ftemp=DistancePointF(pointF[i],ZArray[j])
                if ftemp<dis:
                    stdtemp=j
                    dis=ftemp
            SAArray[stdtemp][N[stdtemp]].x=pointF[i].x
            SAArray[stdtemp][N[stdtemp]].y=pointF[i].y
            N[stdtemp]=N[stdtemp]+1
        for i in range(Nc):
            print "第%d个聚类中心是:(%d,%d)拥有%d个元素   "%(i,ZArray[i].x,ZArray[i].y,N[i])
            print "包含的元素有："
            for j in range(N[i]):
                print "(%d,%d)"%(SAArray[i][j].x,SAArray[i][j].y)
        step=3   #跳转到第三步
        #break
    if step==3:
        print"第%d步，判断是否可以去掉一些"%step
        for i in range(Nc):
            if N[i]<1: #1也可以为其他形参
                #取消这个样本子集
                for j in range(TotalNum):
                    if pointType[j]==i:
                        pointType[j]=-1
                tr=i
                while(tr<Nc-1):
                    for m in range(N[tr+1]):
                        SAArray[tr][m].x=SAArray[tr+1][m].x
                        SAArray[tr][m].y=SAArray[tr+1][m].y
                    tr=tr+1
                tr=i
                while(tr<Nc-1):
                    N[tr]=N[tr+1]
                    tr=tr+1
                Nc=Nc-1
        step=4
        for i in range(Nc):
            print "第%d个聚类中心是:(%d,%d)   "%(i,ZArray[i].x,ZArray[i].y)
            print "包含的元素有："
            for j in range(N[i]):
                print "(%d,%d)"%(SAArray[i][j].x,SAArray[i][j].y)
    #break
    if step==4:
        print"第%d步，修正各个聚类中心"%step
        for i in range(Nc):
            temx=0
            temy=0
            for j in range(N[i]):
                temx+=SAArray[i][j].x
                temy+=SAArray[i][j].y
            ZArray[i].x=temx/N[i]
            ZArray[i].y=temy/N[i]
            print N[i]
            print "修正后聚类中心%d为(%f，%f)"%(i,ZArray[i].x,ZArray[i].y)
        step=5
    if step==5:
        print"第%d步，计算各聚类域中诸样本与聚类中心的平均距离"%step
        TempAverage=0
        for i in range(Nc):
            for j in range(N[i]):
                TempAverage+=DistancePointF(SAArray[i][j],ZArray[i])
            AverageD[i]=TempAverage/N[i]
            print "聚类%d的平均距离为%3f"%(i,AverageD[i])
            TempAverage=0
        step=6
        #break
    if step==6:
        print"第%d步，计算全部模式样本对应聚类中心的总平均距离"%step
        DAv=0
        for i in range(Nc):
            DAv+=N[i]*AverageD[i]
        DAv/=TotalNum
        print"总平均距离为%f"%DAv
        #break
        step=7
    if step==7:
        print"第%d步，判断转移"%step
        if CountTime>StdTime:
            step=14
            print"迭代次数已经达到%d次转移到第%d步"%(StdTime,step)
        elif Nc<=MaxNumStd:
            step=8
            print"转移到第%d步，将已有的聚类分裂"%step            
        elif CountTime%2==0|Nc>2*MaxNumStd:
            step=11
            print"迭代次数为偶次转移到第%d步"%step
    if step==8:
        print"第%d步，计算各聚类中样本距离标准差"%step
        for i in range(Nc):
            temx=0
            temy=0
            for j in range(N[i]):
                temx+=(SAArray[i][j].x-ZArray[i].x)**2
                temy+=(SAArray[i][j].y-ZArray[i].y)**2
            StdDistance[i].x=(temx/N[i])**0.5
            StdDistance[i].y=(temy/N[i])**0.5
            temx=0.0
            temy=0.0
            print "聚类%d的标准差为（%f，%f）"%(i,StdDistance[i].x,StdDistance[i].y)
        step=9
    if step==9:
        print"第%d步，求每个标准差向量中的最大分量"%step
        for i in range(Nc):
            if StdDistance[i].x>StdDistance[i].y:
                StdDisMax[i]=StdDistance[i].x
                StdDisMaxCor[i]=1
            else:
                StdDisMax[i]=StdDistance[i].y
                StdDisMaxCor[i]=0
            print"聚类%d中的标准差最大分量是%d为%f"%(i,StdDisMaxCor[i],StdDisMax[i]) 
        step=10
    if step==10:
        print"第%d步，分裂判断和计算"%step
        temp1=point()
        temp2=point()
        Garma=0.5
        for i in range(Nc):
            if StdDisMax[i]>MaxDiff:
                if((AverageD[i]>DAv)&(N[i]>2*(Nc+1)))|Nc<=MaxNumStd/2:
                    if StdDisMaxCor[i]==0:
                        temp1.x=ZArray[i].x+StdDisMax[i]*Garma
                        temp1.y=ZArray[i].y
                        temp2.x=ZArray[i].x-StdDisMax[i]*Garma
                        temp2.y=ZArray[i].y
                    elif StdDisMaxCor[i]==1:
                        temp1.y=ZArray[i].y+StdDisMax[i]*Garma
                        temp1.x=ZArray[i].x
                        temp2.y=ZArray[i].y-StdDisMax[i]*Garma
                        temp2.x=ZArray[i].x
                    ZArray[i].x=temp1.x
                    ZArray[i].y=temp1.y
                    ZArray[Nc].x=temp2.x
                    ZArray[Nc].y=temp2.y
                    print"聚类%d被分裂为聚类%d和聚类%d"%(i,i,Nc)
                    print"分裂后的中心分别为（%f,%f）和（%f,%f）"%(temp1.x,temp1.y,temp2.x,temp2.y)
                    Nc=Nc+1
                    step=2
                    i=Nc
        step=11
    if step==11:
        print"第%d步，计算全部聚类中心的距离"%step
        rank=0
        for i in range(Nc-1):
            j=i+1
            while(j<Nc):
                ZDistance[rank]=DistancePointF(ZArray[i],ZArray[j])
                ZDistanceR[rank]=j
                ZDistanceC[rank]=i
                print"聚类%d与聚类%d之间的距离为%f"%(i,j,ZDistance[rank])
                rank+=1
                j=j+1
        step=12
        #break
    if step==12:
        print"第%d步，找出类间距离最小的,只考虑一次只合并一对聚类中心的情况"%step
        ZDistanceT=ZDistance[0]
        ZDistanceCT=ZDistanceC[0]
        ZDistanceRT=ZDistanceR[0]
        for i in range(rank):
            if ZDistance[i]<ZDistanceT:
                ZDistanceT=ZDistance[i]
                ZDistanceCT=ZDistanceC[i]
                ZDistanceRT=ZDistanceR[i]
        print "最小的聚类距离为聚类%d和%d之间的距离为%f"%(ZDistanceCT,ZDistanceRT,ZDistanceT)
        step=13
        #break
    if step==13:
        print"第%d步，合并聚类"%step
        if(ZDistanceT<MinDistance):
            ZArrayT=point()
            print"可以进行合并聚类,合并聚类聚类%d和%d生成新聚类%d"%(ZDistanceCT,ZDistanceRT,ZDistanceCT)
            ZArrayT.x=(N[ZDistanceCT]*ZArray[ZDistanceCT].x+N[ZDistanceRT]*ZArray[ZDistanceRT].x)/(N[ZDistanceCT]+N[ZDistanceRT])
            ZArrayT.y=(N[ZDistanceCT]*ZArray[ZDistanceCT].y+N[ZDistanceRT]*ZArray[ZDistanceRT].y)/(N[ZDistanceCT]+N[ZDistanceRT])
            print "聚类中心（%f,%f）聚类中心（%f，%f）合并得出的新的聚类中心为（%f,%f）"%(ZArray[ZDistanceCT].x,ZArray[ZDistanceCT].y,ZArray[ZDistanceRT].x,ZArray[ZDistanceRT].y,ZArrayT.x,ZArrayT.y)
            ZArray[ZDistanceCT].x=ZArrayT.x
            ZArray[ZDistanceCT].y=ZArrayT.y
            i=ZDistanceCT
            while(i<Nc-1):
                ZArray[i].x=ZArray[i+1].x
                ZArray[i].y=ZArray[i+1].y
                i=i+1
            i=ZDistanceCT
            while(i<Nc-1):
                N[i]=N[i+1]
                i+=1
            Nc=Nc-1
        step=14
        #break
    if step==14:
        print"第%d步，最后一步显示结果"%step
        if CountTime>StdTime:
            print"ISODATA算法完毕一共分为%d类"%Nc
            for i in range(Nc):
                print "第%d个聚类中心是:(%f,%f)拥有%d个元素   "%(i,ZArray[i].x,ZArray[i].y,N[i])
                print "包含的元素有："
                for j in range(N[i]):
                    print "(%f,%f)"%(SAArray[i][j].x,SAArray[i][j].y)
            break
        else:
            step=2
