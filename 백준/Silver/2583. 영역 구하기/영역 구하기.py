import sys                                            # 재귀 limit
sys.setrecursionlimit(10000)

M, N, K = map(int,input().split())

arr = []
for _ in range(K):
    arr.append(list(map(int,input().split())))       # 입력 

graph = [[0] *N for _ in range(M)]

for coord in arr:
    a, b, c, d = coord
    for i in range(a,c):
        for j in range(b,d):
            graph[j][i] = 1                          # 그래프만들기 + 직사각형 칠해두기

dxy = [[-1,0],[1,0],[0,1],[0,-1]]                    # 4방향
 
def DFS(x,y):                                        # DFS 재귀함수
    global cnt                        
    graph[x][y] = 1                                  # 방문처리 -> 좌표안넘고 아직방문안했으면 cnt 1 더해주고 그 위치에서 DFS
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<M) and (0<=dy<N):
            if graph[dx][dy] == 0:
                cnt += 1
                DFS(dx,dy)
    
hubo = []                                           # 후보군 넣기, 방문안한 좌표들마다 cnt 1로 초기화해주고 후보군에 넣기
cnt = 1
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            DFS(i,j)
            hubo.append(cnt)
            cnt = 1

hubo.sort()

print(len(hubo))                                   # 답변 출력
for _ in hubo:
    print(_, end = " ")