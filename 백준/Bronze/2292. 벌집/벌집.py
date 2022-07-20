N=int(input())
res=0
count=1
N-=1

while N>0:
    N-=count*6
    res+=1
    count+=1

print(res+1)