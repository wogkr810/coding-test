from collections import deque

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(input()))

hubo = []
dxy = [[1,0],[0,-1],[0,1],[-1,0]] 

one_list = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            one_list.append([i,j])

visited = [[False] * N for _ in range(N)]
queue = deque()

while one_list:
    cnt = 0
    one_x, one_y = one_list.popleft()
    if visited[one_x][one_y]:
        continue
    else:
        visited[one_x][one_y] = True
        queue.append([one_x,one_y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if (0<=dx<N) and (0<=dy<N):
                if not visited[dx][dy] and arr[dx][dy]=='1':
                    visited[dx][dy] = True
                    queue.append([dx,dy])
                    cnt += 1
    hubo.append(cnt+1)

hubo.sort()
print(len(hubo))
for i in hubo:
    print(i)

