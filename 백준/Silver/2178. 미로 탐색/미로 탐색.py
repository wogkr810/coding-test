from collections import deque

N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))
    
dxy = [[1,0],[0,-1],[0,1],[-1,0]]

visited = [[0] * M for _ in range(N)]

visited[0][0] = 1
queue=deque([[0,0]])

while queue:
    x, y = queue.popleft()
    if (x,y) == (N-1,M-1):
        break
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<N) and (0<=dy<M):
            if visited[dx][dy]==0 and arr[dx][dy]=='1':
                visited[dx][dy] = visited[x][y] +1
                queue.append([dx,dy])

print(visited[N-1][M-1])