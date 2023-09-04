from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    tmp_arr = list(map(int,input().split()))
    if tmp_arr[-1] == -1:
        tmp_arr.pop()
        root = tmp_arr.pop(0)
        tmp_arr = [[tmp_arr[i],tmp_arr[i+1]] for i in range(0,len(tmp_arr),2)]

    for v, cost in tmp_arr:
        graph[root].append([v,cost])
        graph[v].append([root,cost])


def bfs(start,visited):
    q = deque([[start,0]])
    visited[start] = 1

    while q:
        v, cost = q.popleft()
        for a,b in graph[v]:
            if not visited[a]:
                visited[a] += (b+visited[v])
                q.append([a,b])
		
    max_value, max_idx = -1, -1
    for i in range(len(visited)):
            if visited[i] >= max_value:
                    max_value = visited[i]
                    max_idx = i		

    # max_value = max(visited)
    # max_idx = visited.index(max_value)
    return max_value, max_idx

value, idx = bfs(1,[0] * (N+1))
ans, idx_2 = bfs(idx, [0] * (N+1))

print(ans-1)

    