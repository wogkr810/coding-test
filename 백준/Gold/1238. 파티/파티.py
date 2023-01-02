import heapq
import sys

def dijkstra(start):
  q=[]
  heapq.heappush(q, (0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

N, M, X = map(int,sys.stdin.readline().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,sys.stdin.readline().split())))

ans_sum_list = [0] * (N+1) 
INF = int(1e9)

for j in range(2):
    distance = [0] + [INF]*(N)
    graph = [[] for i in range(N+1)]
    for node in arr:
        if j == 0: 
            a,b,c = node
            graph[a].append((b,c))
        else:
            a,b,c = node
            graph[b].append((a,c))

    dijkstra(X)
    
    ans_sum_list = [x+y for x,y in zip(ans_sum_list,distance)]

print(max(ans_sum_list))