from collections import deque

M, N = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

queue = deque()

in_tamato = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            in_tamato.append([i,j])

while in_tamato:
    x, y = in_tamato.popleft()
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<N) and (0<=dy<M):
            if arr[dx][dy] == 0:
                arr[dx][dy] = arr[x][y] + 1
                in_tamato.append([dx,dy])

flag = True
max_value = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = False
        if max_value <= arr[i][j]:
            max_value = arr[i][j]

if not flag:
    print(-1)
else:
    print(max_value-1)