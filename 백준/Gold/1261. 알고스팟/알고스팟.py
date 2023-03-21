from collections import deque

N, M = map(int,input().split())
arr = []
for _ in range(M):
    arr.append(list(input()))

dxy = [[-1,0], [0,1], [0,-1],[1,0]]

visited = [[[i,j,0,0] for i in range(N)] for j in range(M)]

visited[0][0][3] = 1
q = deque([[0,0,0,0]])

while q:
    x, y , tmp_cnt , vst = q.popleft()
    if (x,y) == (M-1, N-1):
        break
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<M) and (0<=dy<N):
            if not visited[dx][dy][3]:
                if arr[dx][dy] == '1':
                    visited[dx][dy][3] = 1
                    visited[dx][dy][2] = tmp_cnt + 1
                    q.append([dx,dy,tmp_cnt+1,1])
                else:
                    visited[dx][dy][3] = 1
                    visited[dx][dy][2] = tmp_cnt
                    q.appendleft([dx,dy,tmp_cnt,1])

print(visited[M-1][N-1][2])
