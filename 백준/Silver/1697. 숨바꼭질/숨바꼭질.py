from collections import deque

N, K = map(int,input().split())

flag = True

if N> K:
    ans = N-K
    flag = False

x = min(N,K)
y = max(N,K)
visited = [0] * (2*y+1)
visit_set = set()

queue = deque([x])
visited[x] = 1
visit_set.add(x)
while queue:
    v = queue.popleft()
    if v==y:
        break
    for i in set([v-1,v+1,2*v]):
        if 1<=i<2*y and i not in visit_set:
            visit_set.add(i)
            queue.append(i)
            if visited[i] == 0:
                visited[i] = visited[v] + 1
            else:
                visited[i] = min(visited[v]+1, visited[i])

if not flag:
    print(ans)
else:
    print(visited[y] -1)
