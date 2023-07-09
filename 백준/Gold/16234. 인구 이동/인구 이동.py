from collections import deque


N, L, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dxy = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(a, b, visited):
    q = deque([[a,b]])
    visited[a][b] = True
    res = [[a,b]]

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if (0<=dx<N) and (0<=dy<N):
                if not visited[dx][dy]:
                    if L <= abs(arr[dx][dy] - arr[x][y]) <= R:
                        visited[dx][dy] = True
                        res.append([dx,dy])
                        q.append([dx,dy])    
    return res   

cnt = 0

while True:
    visited = [[False] * N for _ in range(N)]
    tmp_cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                res = bfs(i, j, visited)
                tmp_cnt += 1
                tmp_sum = int(sum([arr[a][b] for a, b in res]) / len(res))
                for x_idx, y_idx in res:
                    arr[x_idx][y_idx] = tmp_sum

    if tmp_cnt == N**2:
        break
    else:
        cnt += 1

print(cnt)