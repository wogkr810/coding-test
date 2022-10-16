from collections import defaultdict, deque

def solution(n, wires):
    hubo = []
    wires = deque(wires)
    cnt = n-1
    while cnt:
        cnt -= 1
        a, b = wires.popleft()
        graph = defaultdict(list)
        for wire in wires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])


        ans = []
        for _ in [a,b]:
            visited = [False] * (n+1)
            visited[_] = True
            visit_count = 0
            try:
                q = deque([_,graph[_][0]])
            except:
                q = deque()
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if not visited[w]:
                        visited[w] = True
                        q.append(w)
                        visit_count +=1
            ans.append(visit_count)
        wires.append([a,b])
        hubo.append(abs(ans[0]-ans[1]))
    
    return min(hubo)