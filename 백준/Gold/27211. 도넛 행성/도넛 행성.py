from collections import deque

N, M = map(int,input().split())
arr = []
hubo = []
for i in range(N):
    tmp_list = list(map(int,input().split()))
    for j in range(M):
        if tmp_list[j] == 0:
            hubo.append([i,j])
    arr.append(tmp_list)

dxy = [[0,1],[0,-1],[1,0],[-1,0]]
hubo = deque(hubo)
cnt = 0

while hubo:
    start_x, start_y = hubo.popleft()
    q = deque([[start_x,start_y]])

    if arr[start_x][start_y] == 1:
        continue
    else:
        cnt += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx = (x + dxy[i][0]) %N
            dy = (y + dxy[i][1]) %M
            if arr[dx][dy] == 0:
                q.append([dx,dy])
                arr[dx][dy] = 1

print(cnt)