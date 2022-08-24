from bisect import bisect, bisect_left

N=int(input())
arr=list(map(int,input().split()))

dp=[arr[0]]

for i in range(len(arr)):
    if dp[-1]<arr[i]:
        dp.append(arr[i])
    else:
        idx=bisect_left(dp,arr[i])
        dp[idx]=arr[i]

print(len(dp))