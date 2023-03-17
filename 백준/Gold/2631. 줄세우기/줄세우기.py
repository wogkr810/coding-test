N = int(input())
arr = [int(input()) for _ in range(N)]

dp = [1] *(N)

for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] +1 ,dp[i])

print(N-max(dp))