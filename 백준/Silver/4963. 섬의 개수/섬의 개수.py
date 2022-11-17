import sys
sys.setrecursionlimit(10000)

dxx = [-1,-1,-1,0,0,1,1,1]
dyy = [1,0,-1,1,-1,1,0,-1]

def DFS(x,y):
    visited[x][y] = True
    for i in range(8):
        dx = x + dxx[i]
        dy = y + dyy[i]
        if (0<=dx<h) and (0<=dy<w):
            if not visited[dx][dy] and arr[dx][dy] == 1:
                DFS(dx,dy)


while True:
    w, h = map(int,input().split())
    if (w,h) == (0,0):
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int,input().split())))
    visited = [[False] * w for _ in range(h)]
    land = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                land.append([i,j])
    cnt = 0
    while land:
        x,y = land.pop()
        if not visited[x][y]:
            cnt += 1
        DFS(x,y)
    
    print(cnt)
    
    