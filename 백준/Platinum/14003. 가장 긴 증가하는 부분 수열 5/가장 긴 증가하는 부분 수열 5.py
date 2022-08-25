from bisect import bisect, bisect_left

N=int(input())
arr=list(map(int,input().split()))

dp_count=[1 for _ in range(N)]
dp=[arr[0]]

for i in range(len(arr)):
    if dp[-1]<arr[i]:
        dp.append(arr[i])
        dp_count[i]=len(dp)
    else:
        idx=bisect_left(dp,arr[i])
        dp[idx]=arr[i]
        dp_count[i]=idx+1
   
max_dp=max(dp_count)
res=[]
for i in range(N-1,-1,-1):
    if dp_count[i]==max_dp:
        res.append(arr[i])
        max_dp-=1

res=res[::-1]

print(len(res))
for i in res:
    print(i, end = " ")