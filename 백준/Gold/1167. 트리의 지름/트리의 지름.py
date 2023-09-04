import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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


def dfs(v,cost):
    for a,b in graph[v]:
        if distance[a] == -1:
            distance[a] = cost + b
            dfs(a,cost+b)

distance = [-1] * (N+1)
distance[1] = 0
dfs(1,0)

max_value = max(distance)
max_idx = distance.index(max_value)

distance = [-1] * (N+1)
distance[max_idx] = 0
dfs(max_idx,0)

print(max(distance))
