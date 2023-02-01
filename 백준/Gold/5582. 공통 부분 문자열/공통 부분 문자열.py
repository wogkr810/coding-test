S = input()
T = input()

len_s = len(S)
len_t = len(T)
dp = [[0] * (len_t+1) for _ in range(len_s+1)]

answer = 0 

for i in range(1,len_s+1):
    for j in range(1,len_t+1):
        if S[i-1] == T[j-1]: 
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)