N = int(input())

if N==1:
    print(0)
    print(1)
    exit(0)
dp = [0] + [0 for i in range(N)]
flag_list = [0,1]
for i in range(2,N+1):
    flag = 0
    dp[i] = dp[i-1] + 1
    flag = 1
    if i%3 == 0:
        if dp[i//3] +1 < dp[i]:
            dp[i] = dp[i//3] + 1
            flag = 2
    if i%2 == 0:
        if dp[i//2] +1 < dp[i]:
            dp[i] = dp[i//2] + 1
            flag = 3
    flag_list.append(flag)

hubo = [N]
while True:
    tmp = N
    if flag_list[N] == 1:
        hubo.append(N-1)
        N = N-1
    elif flag_list[N] == 2:
        hubo.append(N//3)
        N = N//3
    elif flag_list[N] == 3:
        hubo.append(N//2)
        N = N//2
    if N<=1:
        break

print(len(hubo)-1)
print(*hubo)