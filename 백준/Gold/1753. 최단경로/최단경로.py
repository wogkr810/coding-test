import heapq
from collections import defaultdict
import sys
sys = sys.stdin.readline

V, E = map(int,input().split())
s = int(input())

INF = int(1e9)
graph = [dict() for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a, b, c = map(int,input().split())
    if b in graph[a]:
        if c < graph[a][b]:
            graph[a][b] = c
    else:
        graph[a][b] = c 

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for key,value in graph[now].items():
            cost = dist + value
            if cost < distance[key]:
                distance[key] = cost
                heapq.heappush(q,(cost,key))

dijkstra(s)

for i in range(1, V+1):
    if i == s:
        print(0)
    else:
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])
