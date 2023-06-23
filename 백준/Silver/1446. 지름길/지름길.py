import heapq

N, D = map(int,input().split())
graph = [[] for _ in range(D+1)]
distance = [D+1] * (D+1)

for _ in range(N):
    a, b, c = map(int,input().split())
    if (b <= D) and (b-a > c):
        graph[a].append([b,c])

for i in range(D):
    graph[i].append([i+1,1])


q = []
distance[0] = 0 
heapq.heappush(q,(0,0))

while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = i[1] + dist
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[D])
