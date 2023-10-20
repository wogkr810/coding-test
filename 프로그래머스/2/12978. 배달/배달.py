import heapq

def dijkstra(start,distance,graph):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for rd in road:
        a, b, c = rd
        graph[a].append([b,c])
        graph[b].append([a,c])

    INF = int(1e9)
    distance = [INF] * (N+1)
    
    dijkstra(1, distance, graph)

    ans = 0
    for i in distance[1:]:
        if i <= K:
            ans += 1
    
    return ans