import heapq
import sys

input = sys.stdin.readline

while True:
    N, M = map(int,input().split()) 
    graph = [[] for _ in range(N+1)] 
    visited = [False] * (N+1) 
    total_cost = 0
    if (N,M) == (0,0):
        break
    for _ in range(M):
        u, v, c = list(map(int,input().split()))
        graph[u].append([c, u, v])
        graph[v].append([c, v, u])
        total_cost += c


    def prim(start):
        visited[start] = True
        q = graph[start]
        heapq.heapify(q)
        mst = []
        cost = 0
        
        while q:
            c, u, v = heapq.heappop(q)
            if not visited[v]:
                visited[v] = True
                mst.append((u,v))
                cost += c
                for edge in graph[v]:
                    if not visited[edge[2]]:
                        heapq.heappush(q, edge)
                

        return mst, cost

    mst, weight = prim(1)
    print(total_cost - weight)