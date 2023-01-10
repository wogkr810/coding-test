from collections import deque

N = int(input())
T = int(input())

arr = [[0] * N for _ in range(N)]
arr[N//2][N//2] = 1

dxy = deque([[-1,0],[0,1],[1,0],[0,-1]]*(N//2)) 

cnt = 1
num = 1

(x,y) = (N//2, N//2)

while dxy:
    x_dir_1, y_dir_1 = dxy.popleft()
    x_dir_2, y_dir_2 = dxy.popleft()
    
    for i in range(cnt):
        x,y = (x + x_dir_1, y + y_dir_1)
        num += 1
        arr[x][y] = num


    for j in range(cnt):
        x,y = (x + x_dir_2, y + y_dir_2)
        num += 1
        arr[x][y] = num

    cnt += 1

for j in range(0, N-1):
    arr[j][0] = N**2-j

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        if arr[i][j] == T:
            (ans_x, ans_y) = (i+1,j+1)
    print()

print(ans_x, ans_y)
