def spi(n):
    dp=[1,1,1,2,2]
    for i in range(5,n+1):
        dp.append(dp[i-1]+dp[i-5])
    return dp[n-1]

T=int(input())
for i in range(T):
    N=int(input())
    print(spi(N))