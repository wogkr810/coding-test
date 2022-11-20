from collections import deque
from copy import deepcopy

N = int(input())
arr1 = []
for _ in range(N):
    arr1.append(list(input()))

visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]

dxy = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(x,y,color,visited,arr):
    queue = deque([[x,y]])
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if (0<=dx<N) and (0<=dy<N):
                if not visited[dx][dy] and arr[dx][dy] == color:
                    queue.append([dx,dy])
                    visited[dx][dy] = True

cnt1 = 0
cnt2 = 0

arr2 = deepcopy(arr1)

for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i,j,arr1[i][j],visited1,arr1)
            cnt1 +=1
        if not visited2[i][j]:
            bfs(i,j,arr2[i][j],visited2,arr2)
            cnt2 +=1
        
print(cnt1,cnt2)