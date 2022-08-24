N = int(input())
arr=list(map(int,input().split()))

dp=[1 for _ in range(N)]
lis_list=[[] for _ in range(N)]

for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)

max_index=max(dp)
    

res=[]
for i in range(N-1,-1,-1):
    if dp[i]==max_index:
        res.append(arr[i])
        max_index-=1

res=res[::-1]

print(len(res))
for i in res:
    print(i, end=" ")