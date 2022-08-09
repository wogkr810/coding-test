from collections import defaultdict
import math

def hh_mm(time):
    return int(time[:2])*60 + int(time[3:])

def solution(fees, records):

    dt=defaultdict(list)
    for i in records:
        dt[i.split()[1]].append((hh_mm(i.split()[0]),i.split()[2]))
        
    dt=list(sorted(dt.items()))
    total_minute=[]
    for car in dt:
        cnt=0
        if len(car[1])%2==0:
            for i in range(0,len(car[1]),2):
                cnt+=(car[1][i+1][0]-car[1][i][0])
        else:
            for i in range(0,len(car[1])-2,2):
                cnt+=(car[1][i+1][0]-car[1][i][0])
            cnt+=(hh_mm("23:59")-car[1][-1][0])
        total_minute.append(cnt)
        
    res=[]

    for i in total_minute:
        if i<=fees[0]:
            res.append(fees[1])
        else:
            res.append(fees[1]+math.ceil((i-fees[0])/fees[2])*fees[3])

    return res