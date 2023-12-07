import math
from copy import deepcopy
import sys

input = sys.stdin.readline

dxy = [[-1,0], [1,0], [0,-1],[0,1]]

def is_inside(x,y):
    if (0 <= x < R) and (0 <= y < C):
        return True
    return False

R, C, T = map(int,input().split())
arr = []
air = []
for i in range(R):
    tmp_input = list(map(int,input().split()))
    if tmp_input[0] == -1:
        air.append([i,0])
    arr.append(tmp_input)

for _ in range(T):
    tmp_board = deepcopy(arr)

    for i in range(R):
        for j in range(C):
            if tmp_board[i][j] <= 0:
                continue
            cnt = 0
            minus_value = math.floor(arr[i][j]/5)
            for k in range(4):
                dx = i + dxy[k][0]
                dy = j + dxy[k][1]
                if is_inside(dx,dy) and arr[dx][dy] != -1:
                    cnt += 1
                    tmp_board[dx][dy] += minus_value
            tmp_board[i][j] -=  math.floor(minus_value) * cnt   

    arr = deepcopy(tmp_board)
    up_dxy = [[0,1], [-1,0], [0,-1], [1,0]]
    donw_dxy = [[0,1], [1,0], [0, -1], [-1,0]]

    def vt(condition):
        start_d = 0
        if condition == 'up':
            direction = up_dxy
            dest = air[0][0]
        elif condition == 'down':
            direction = donw_dxy
            dest = air[1][0]
        x, y = dest , 1
        before = 0
        while True:
            nx = x + direction[start_d][0]
            ny = y + direction[start_d][1]
            if (x,y) == (dest,0):
                break
            if not is_inside(nx,ny):
                start_d += 1
                continue
            arr[x][y], before = before, arr[x][y]
            x = nx
            y = ny
        
    vt('up')
    vt('down')

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)