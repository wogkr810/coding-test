N = int(input())
arr = [list(input()) for _ in range(N)]

def check_max(x, y, arr, target, N):
    cnt = -1
    r, c = -1, -1
    tmp_r, tmp_c = 0, 0

    for i in range(N):
        if arr[x][i] == target:
            tmp_c += 1
        else:
            tmp_c = 0
        
        if arr[i][y] == target:
            tmp_r += 1
        else:
            tmp_r = 0
        
        r = max(tmp_r, r)
        c = max(tmp_c, c)
    
    cnt = max(r,c)

    return cnt

dxy = [[1,0], [-1,0], [0,1], [0,-1]]

ans = -1
tmp_ans = check_max(0, 0, arr, arr[0][0], N)
ans = max(ans, tmp_ans)

for i in range(N):
    for j in range(N):
        for k in range(4):
            dx = i + dxy[k][0]
            dy = j + dxy[k][1]
            if (0 <= dx < N) and (0 <= dy < N):
                arr[i][j], arr[dx][dy] = arr[dx][dy], arr[i][j]
                tmp_ans = check_max(i, j, arr, arr[i][j], N)
                ans = max(ans, tmp_ans)
                arr[i][j], arr[dx][dy] = arr[dx][dy], arr[i][j]

print(ans)