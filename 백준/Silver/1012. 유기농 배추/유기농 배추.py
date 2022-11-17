import sys
sys.setrecursionlimit(10000)

dxy = [[1,0],[0,-1],[-1,0],[0,1]]

def DFS(x,y):
    global cnt
    arr[y][x] = 0
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<M) and (0<=dy<N):
            if arr[dy][dx] == 1:
                DFS(dx,dy)
                arr[dy][dx] = 0

T = int(input())

for _ in range(T):
    cnt = 0
    M, N, K = map(int,input().split())
    cabbage = []
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        cabbage.append([a,b])
        arr[b][a] = 1
    while cabbage:
        x, y = cabbage.pop()
        if arr[y][x] == 0:
            continue
        else:
            cnt +=1
            DFS(x,y)
    print(cnt)