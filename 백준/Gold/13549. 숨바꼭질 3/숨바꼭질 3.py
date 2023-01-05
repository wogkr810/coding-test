from collections import deque

N, K = map(int,input().split())

q = deque([N])
visited = [-1] * 100001
visited[N] = 0 

while q:
    tmp = q.popleft()
    if tmp == K:
        print(visited[K])
        break
    
    for hubo in [tmp-1, tmp+1, tmp *2]:
        if 0 <= hubo < 100001 and visited[hubo] == -1:
            if hubo == tmp * 2:
                q.appendleft(hubo)
                visited[hubo] = visited[tmp]
            else:
                q.append(hubo)
                visited[hubo] = visited[tmp] + 1 

