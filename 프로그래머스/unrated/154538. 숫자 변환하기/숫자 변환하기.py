def solution(x, y, n):
    dp = [0] * (1000001)
    dp[x] = 1
    for i in range(x,y+1):
        hubo = []
        if dp[i-n]:
            hubo.append(dp[i-n])
        if i%2 ==0 and dp[i//2]:
            hubo.append(dp[i//2])
        if i%3 ==0 and dp[i//3]:
            hubo.append(dp[i//3])

        if hubo:
            dp[i] = min(hubo) + 1
            
    if x == y:
        return 0
    else:
        return dp[y]-1 if (dp[y]-1)!=0 else -1
