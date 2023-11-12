N = int(input())
x, y = map(int,input().split())
M = int(input())
chon = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    chon[a].append(b)
    chon[b].append(a)

visited = [False] * (N+1)
cnt = [0] * (N+1)

def dfs(start, count):
    visited[start] = True
    cnt[start] = count 

    for i in chon[start]:
        if not visited[i]:
            dfs(i, count+1)

dfs(x,0)

if cnt[y] == 0:
    print(-1)
else:
    print(cnt[y])
