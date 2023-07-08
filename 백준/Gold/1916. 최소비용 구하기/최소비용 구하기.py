import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

A, B = map(int,input().split())
dijkstra(A)

print(distance[B])