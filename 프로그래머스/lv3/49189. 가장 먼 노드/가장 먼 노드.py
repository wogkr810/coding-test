from collections import defaultdict,deque

def solution(n, vertex):
    graph = defaultdict(list)
    
    for i in range(len(vertex)):
        a,b = vertex[i]
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)
    visited[1] = 1
    queue = deque([1])
    
    while queue:
        tmp = queue.popleft()
        for v in graph[tmp]:
            if visited[v] == 0:
                visited[v] = visited[tmp] + 1
                queue.append(v)

    return visited.count(max(visited))