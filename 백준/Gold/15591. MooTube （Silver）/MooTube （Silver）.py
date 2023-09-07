from collections import deque

N, Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

Q = [list(map(int,input().split())) for _ in range(Q)]

INF = int(1e10)
for k, v in Q:
    visited = [0] * (N+1)
    q = deque([])
    q.append(v)
    visited[v] = 1
    cnt = 0
    while q:
        now = q.popleft()
        for a, b in graph[now]:
            if not visited[a]:
                if b >= k:
                    visited[a] = 1
                    cnt += 1
                    q.append(a)
    print(cnt)

