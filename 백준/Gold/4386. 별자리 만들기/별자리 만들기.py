import math
import heapq
from itertools import combinations

def find_distance(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
N = int(input())
arr = [0] + [list(map(float,input().split())) for _ in range(N)]
cost_graph = [[0] * (N+1) for _ in range(N+1)]

for combination in combinations([i for i in range(1,N+1)],2):
    a, b = combination
    dist = find_distance(arr[a][0], arr[b][0], arr[a][1], arr[b][1])
    cost_graph[a][b] = dist
    cost_graph[b][a] = dist

graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i != j:
            graph[i].append([cost_graph[i][j], i, j])

visited = [False] * (N+1)
def prim(start):
    visited[start] = True
    mst = []
    q = graph[start]
    heapq.heapify(q)
    cost = 0

    while q:
        c, a, b = heapq.heappop(q)
        if not visited[b]:
            visited[b] = True
            cost += c
            mst.append((a,b))
            for edge in graph[b]:
                if not visited[edge[2]]:
                    heapq.heappush(q,edge)
    return mst,cost

print(round(prim(1)[1],2))