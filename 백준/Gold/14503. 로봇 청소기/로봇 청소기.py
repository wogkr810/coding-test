N, M = map(int,input().split())
X, Y, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dxy = [[-1,0], [0,1], [1,0], [0,-1]]
cnt = 0

def dfs(x, y, d):
    global cnt
    if arr[x][y] == 0:
        cnt += 1
        arr[x][y] = 2
    
    for i in range(4):
        dv = (d+3) % 4
        dx = x + dxy[dv][0]
        dy = y + dxy[dv][1]
        if arr[dx][dy] == 0:
            dfs(dx, dy, dv)
            return 
        d = dv
    

    new_d = (d+2) % 4
    dx = x + dxy[new_d][0]
    dy = y + dxy[new_d][1]
    if arr[dx][dy] == 1:
            return
    dfs(dx,dy,d)


dfs(X,Y,D)
print(cnt)
    