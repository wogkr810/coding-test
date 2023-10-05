from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int,input().split())
arr = []
for i in range(N):
    tmp_list = list(map(int,input().split()))
    for j in range(M):
        if tmp_list[j] == 2:
            gram = [i,j]
    arr.append(tmp_list)

dxy = [[1,0],[0,1],[0,-1],[-1,0]]
q = deque([[0,0]])
visited = [[0] * M for _ in range(N)]
ans = int(1e10)

for i in range(2):
    q = deque([[0,0]])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    if i == 0:
        while q:
            x, y = q.popleft()
            for i in range(4):
                dx = x + dxy[i][0]
                dy = y + dxy[i][1]
                if (0<=dx<N) and (0<=dy<M):
                    if not visited[dx][dy]:
                        if arr[dx][dy] == 0:
                            visited[dx][dy] = visited[x][y] + 1
                            q.append([dx,dy])

        if visited[N-1][M-1] != 0:
            ans = min(ans, visited[N-1][M-1]-1)
    
    else:
        # 그람 찾고, 그람에서 다시 시작 -> 그람 visited가 0 이아니면 break

        while q:
            x, y = q.popleft()
            for i in range(4):
                dx = x + dxy[i][0]
                dy = y + dxy[i][1]
                if (0<=dx<N) and (0<=dy<M):
                    if not visited[dx][dy]:
                        if arr[dx][dy] != 1:
                            visited[dx][dy] = visited[x][y] + 1
                            q.append([dx,dy])

        gram_xy = visited[gram[0]][gram[1]]
        if gram_xy == 0:
            break
        visited = [[0] * M for _ in range(N)]
        visited[gram[0]][gram[1]] = gram_xy
        q = deque([[gram[0],gram[1]]])

        while q:
            x, y = q.popleft()
            for i in range(4):
                dx = x + dxy[i][0]
                dy = y + dxy[i][1]
                if (0<=dx<N) and (0<=dy<M):
                    if not visited[dx][dy]:
                        visited[dx][dy] = visited[x][y] + 1
                        q.append([dx,dy])

        if visited[N-1][M-1] != 0:
            ans = min(ans, visited[N-1][M-1]-1)

if ans > T:
    print('Fail')
else:
    print(ans)

