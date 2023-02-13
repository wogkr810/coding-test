from collections import defaultdict
import heapq

N, M = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

INF = 1e9
visited = [False] * (N+1)
distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q,(cost,v[0]))

dijkstra(1)
print(distance[N])