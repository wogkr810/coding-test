from collections import deque
import sys

N, M, R = map(int,sys.stdin.readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

for i in range(len(G)):
    G[i].sort()
    

visited=[False]*(N+1)
visited[R]=True
res=[0]*(N+1)
queue=deque([R])
cnt=1
while queue:
    tmp=queue.popleft()
    res[tmp]=cnt
    cnt+=1
    for i in G[tmp]:
        if not visited[i]:
            queue.append(i)
            visited[i]=True

for i in res[1:]:
    print(i)