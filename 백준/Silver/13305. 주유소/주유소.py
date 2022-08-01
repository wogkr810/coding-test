N=int(input())
d=list(map(int,input().split()))
cost=list(map(int,input().split()))

cnt=0
m=1e10

for i in range(len(cost)-1):
    if cost[i]<m:
        m=cost[i]
    cnt+=m*d[i]

print(cnt)