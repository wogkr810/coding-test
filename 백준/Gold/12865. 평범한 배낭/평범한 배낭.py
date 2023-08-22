N, K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
arr = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N+1):
    weight, value = arr[i]
    for j in range(1,K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])