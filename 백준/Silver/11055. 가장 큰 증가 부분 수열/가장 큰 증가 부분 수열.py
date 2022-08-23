N=int(input())
arr=list(map(int,input().split()))

dp=[0 for _ in range(N)]
dp[0]=arr[0]

for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(arr[i]+dp[j],dp[i])
        else:
            dp[i]=max(dp[i],arr[i])
    # print(dp)
    # print(arr)

print(max(dp))