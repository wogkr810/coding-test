from collections import deque

F, S, G, U, D = map(int,input().split())

q = deque([S])
visited = [0] * (F+1)
visited[S] = 1

if S == G:
    print(0)
else:
    while q:
        now = q.popleft()
        for i in [now+U, now-D]:
            if (1 <= i <= F) and not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)

    if visited[G]:
        print(visited[G]-1)
    else:
        print("use the stairs")
        