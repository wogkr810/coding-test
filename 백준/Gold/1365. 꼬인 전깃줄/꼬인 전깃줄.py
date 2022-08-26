from bisect import bisect_left

N=int(input())
arr=list(map(int,input().split()))

dp=[]

for i in range(len(arr)):
    if len(dp)==0:
        dp.append(arr[i])
    elif dp[-1]<arr[i]:
        dp.append(arr[i])
    else:
        idx=bisect_left(dp,arr[i])
        dp[idx]=arr[i]

print(N-len(dp)) 