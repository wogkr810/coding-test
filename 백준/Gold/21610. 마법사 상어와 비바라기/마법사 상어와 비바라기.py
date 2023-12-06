import sys

input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
direction = [list(map(int,input().split())) for _ in range(M)]

dxy = [[0,0], [0,-1], [-1,-1], [-1, 0], [-1, 1], [0, 1], [1,1], [1,0], [1,-1]]
diag = [[-1,-1], [1,1], [-1,1], [1,-1]]
tmp_cloud = [[N-1,0], [N-1,1], [N-2, 0], [N-2,1]]

for i in range(len(direction)):
    d, cnt = direction[i]
    dxx, dyy = dxy[d][0], dxy[d][1]
    visited = [[False] * N for _ in range(N)]
    clouds = tmp_cloud

    for j in range(len(clouds)):
        clouds[j][0] = (clouds[j][0] + dxx * cnt) % N
        clouds[j][1] = (clouds[j][1] + dyy * cnt) % N
        arr[clouds[j][0]][clouds[j][1]] += 1
        visited[clouds[j][0]][clouds[j][1]] = True

    for x, y in clouds:
        for _ in range(4):
            dx = x + diag[_][0]
            dy = y + diag[_][1]
            if (0 <= dx < N) and (0 <= dy < N):
                if arr[dx][dy] >= 1:
                    arr[x][y] += 1

    tmp_cloud = []
    for p in range(N):
         for q in range(N):
              if arr[p][q] >= 2 and not visited[p][q]:
                   tmp_cloud.append([p,q])
                   arr[p][q] -= 2


ans = 0

for i in range(N):
    for j in range(N):
        ans += arr[i][j]

print(ans)
    