from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def check_arr(arr, r, c, visited):
    rb_cnt = 0
    tmp_check = [[r,c]]
    top_x, top_y = r, c
    q = deque([[r, c]])
    visited[r][c] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if (0<=dx<N) and (0<=dy<N):
                if not visited[dx][dy]:
                    if arr[dx][dy] in [arr[r][c], 0]:
                        q.append([dx,dy])
                        tmp_check.append([dx,dy])
                        visited[dx][dy] = True
                        if arr[dx][dy] == arr[r][c]:
                            top_x = min(top_x, dx)
                            top_y = min(top_y, dy)
                        elif arr[dx][dy] == 0:
                            rb_cnt += 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and visited[i][j]:
                visited[i][j] = False
                
    return tmp_check, rb_cnt, top_x, top_y, len(tmp_check)  

def gravity(arr):
    N = len(arr[0])
    for i in range(N-1):
        for j in range(N):
            p = i
            while 0<=p and arr[p][j] not in [-1,-2] and arr[p+1][j] == -2:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1

def rotated_270(arr):
  n = len(arr)
  result = [[0]* n for _ in range(n)] # 배열의 가로 세로 길이가 뒤바뀌는 것 주의
  for i in range(n): # 범위 주의
    for j in range(n): # 범위 주의
      result[n-1-j][i] = arr[i][j]
  return result
        

dxy = [[0,1], [0,-1], [1,0], [-1,0]]
score = 0

while True:
    visited = [[False] * N for _ in range(N)]
    color = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] not in [0, -1, -2] and not visited[i][j]:
                tmp_check, rainbow_cnt, x, y, length = check_arr(arr, i, j, visited)
                if length >= 2:  
                    color.append([length, rainbow_cnt, x, y, tmp_check, arr[i][j]])  

    if not color:
        break

    color.sort(key = lambda x : (-x[0],-x[1], -x[2], -x[3]))

    score += color[0][0] ** 2

    for remove_x, remove_y in color[0][4]:
        arr[remove_x][remove_y] = -2

    gravity(arr)
    arr = rotated_270(arr)
    gravity(arr)
    

print(score)