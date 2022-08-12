from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])

    visited=[[False]*m for _ in range(n)]
    distance=[[0]*m for _ in range(n)]
    visited[0][0]=True
    distance[0][0]=1

    que=deque([[0,0]])
    cnt=1
    while que:
        x , y = que.popleft()
        dx=[1, 0, -1, 0]
        dy=[0, 1, 0, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                if maps[nx][ny]== 1:
                    que.append([nx, ny])
                    visited[nx][ny]=True
                    distance[nx][ny]=distance[x][y]+1



    if distance[n-1][m-1]==0:
        return -1
    else:
        return distance[n-1][m-1]