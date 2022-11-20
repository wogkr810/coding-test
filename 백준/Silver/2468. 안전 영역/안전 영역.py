import sys
sys.setrecursionlimit(10000)

N = int(input())

arr = []
max_value = 0
for _ in range(N):
    tmp_list = list(map(int,input().split()))
    if max(tmp_list) >= max_value:
        max_value = max(tmp_list)
    arr.append(tmp_list)

def DFS(x,y,value):
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<N) and (0<=dy<N) and not visited[dx][dy] and arr[dx][dy] > value:
            visited[dx][dy] = True
            DFS(dx,dy,value)

dxy = [[-1,0],[1,0],[0,1],[0,-1]]

ans = 1

for k in range(1,max_value+1):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]:
                DFS(i,j,k)
                cnt += 1
    ans = max(ans,cnt)

print(ans)
