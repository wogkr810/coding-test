from collections import deque
import sys

M, N, H = map(int,sys.stdin.readline().split())
arr = []
flag1 = True
one_tomato = deque()
dxyz = [[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,0,0],[-1,0,0]]

for i in range(H):
    tmp_arr = []
    for j in range(N):
        tmp_arr.append(list(map(int,sys.stdin.readline().split())))
        for k in range(M):
            if tmp_arr[j][k] == 1:
                one_tomato.append([i,j,k])
            if tmp_arr[j][k] == 0:
                flag1 = False   
    arr.append(tmp_arr)

while one_tomato:
    z, y, x = one_tomato.popleft()
    for i in range(6):
        dx = x + dxyz[i][2] 
        dy = y + dxyz[i][1]
        dz = z + dxyz[i][0]
        if (0<=dx<M) and (0<=dy<N) and (0<=dz<H):
            if arr[dz][dy][dx] == 0:
                arr[dz][dy][dx] = arr[z][y][x] + 1
                one_tomato.append([dz,dy,dx])

max_value = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            max_value = max(max_value,arr[i][j][k])
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)

if flag1:
    print(0)
else:
    print(max_value-1)


