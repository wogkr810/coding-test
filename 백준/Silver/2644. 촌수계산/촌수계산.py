from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

N = int(input())
X, Y = map(int,input().split())
T = int(input())
arr = []
for _ in range(T):
    arr.append(list(map(int,input().split())))

graph = defaultdict(list)
visited = [False] * (N+1)

for a,b in arr:
    graph[a].append(b)
    graph[b].append(a)

flag = True

def DFS(start,end,cnt):
    global flag
    if start == end:
        print(cnt)
        flag = False
        return 
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            DFS(v,end,cnt+1)

DFS(X,Y,0)
if flag:
    print(-1)
            
