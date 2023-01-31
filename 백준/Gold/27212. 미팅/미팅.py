N, M ,C = map(int,input().split())
W = []
for _ in range(C):
    W.append(list(map(int,input().split())))

A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        case_1 = dp[i-1][j-1] + W[A[i-1]-1][B[j-1]-1]
        case_2 = dp[i][j-1]
        case_3 = dp[i-1][j]
        dp[i][j] = max(case_1, case_2, case_3)

print(dp[N][M])