N, K = map(int,input().split())
S = list(input())

visited = [False] * N
cnt = 0

for i in range(N):
    if S[i] == 'H':
        continue
    elif S[i] == 'P':
        flag = True
        for j in range(i-K, i):
            if j >= 0 and not visited[j] and S[j] == 'H':
                cnt += 1
                visited[j] = True
                flag = False
                break

        if flag:
            for k in range(i+1, i+1+K):
                if k < N and not visited[k] and S[k] == 'H':
                    cnt += 1
                    visited[k] = True
                    break

print(cnt)            