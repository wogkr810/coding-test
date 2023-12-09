def odd_even(arr):
    odd = True
    even = True
    for i in arr:
        if i % 2 == 0:
            continue
        else:
            even = False
            break
    for i in arr:
        if i % 2 == 1:
            continue
        else:
            odd = False
    if odd or even:
        return True
    else:
        return False
    
N, M, K = map(int,input().split())

dxy = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    arr[r-1][c-1].append([m,s,d])

for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != []:
                for m, s, d in arr[i][j]:
                    r = (i + dxy[d][0] * s) % N
                    c = (j + dxy[d][1] * s) % N
                    board[r][c].append([m,s,d])

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                tmp_mass, tmp_s, dd = 0, 0, []
                for m, s, d in board[i][j]:
                    tmp_mass += m
                    tmp_s += s
                    dd.append(d)
                
                tmp_mass = tmp_mass //5
                if tmp_mass == 0:
                    board[i][j] = []
                    continue
                tmp_s = tmp_s // len(board[i][j])

                d_flag = odd_even(dd)
                if d_flag:
                    board[i][j] = []
                    for k in range(0,8,2):
                        board[i][j].append([tmp_mass, tmp_s, k])
                else:
                    board[i][j] = []
                    for k in range(1,8,2):
                        board[i][j].append([tmp_mass, tmp_s, k])
        
    arr = [lst[:] for lst in board]

ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != []:
            for m, s, d in arr[i][j]:
                ans += m

print(ans)