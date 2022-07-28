N=int(input())

def fibo(n):
    dp=[1,1]
    for i in range(2,n+1):
        dp.append((dp[i-1]+dp[i-2])%15746)
    return dp[n]

print(fibo(N))