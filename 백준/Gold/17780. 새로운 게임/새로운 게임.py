from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N , K = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(N)]
arr = [[]]
for _ in range(K):
    x, y, d = list(map(int,input().split()))
    arr.append([x-1, y-1, d])

chess = defaultdict(deque)
reverse_dict = {1 : 2, 2 : 1, 3 : 4 , 4 : 3}
direction_dict = {1 : [0,1], 2: [0,-1], 3 : [-1,0], 4 : [1,0]}
    

for i in range(N**2+1):
    chess[i] = deque()

for i in range(1, K+1):
    k_x, k_y, k_d = arr[i]
    chess[(k_x) * N + k_y +1].append(i)


cnt = 0
flag = True

while True:
    for i in range(1,K+1):
        x, y, d = arr[i]
        if chess[(x) * N + y+1][0] == i:
            d_x, d_y = direction_dict[d]
            
            if (0 <= x+d_x < N) and (0 <= y+d_y < N):
                if C[x+d_x][y+d_y] in [0,1]:
                    tmp_deque = chess[(x) * N + y+1]
                    for idx in tmp_deque:
                        arr[idx][0] = (x+d_x)
                        arr[idx][1] = (y+d_y)

                    if C[x+d_x][y+d_y] == 0:
                        chess[(x+d_x) * N + y + d_y+1].extend(tmp_deque)
                    elif C[x+d_x][y+d_y] == 1:
                        tmp_deque.reverse()
                        chess[(x+d_x) * N + y + d_y+1].extend(tmp_deque)

                    chess[(x) * N + y+1] = deque()

                    if len(chess[(x+d_x) * N + y + d_y + 1]) >= 4:
                        flag = False
                        break

                elif C[x+d_x][y+d_y] == 2:
                    d = reverse_dict[d]
                    arr[i][2] = d
                    d_x, d_y = direction_dict[d]
                    if (0 <= x+d_x < N) and (0 <= y+d_y < N) and C[x+d_x][y+d_y] != 2:
                        tmp_deque = chess[(x) * N + y+1]
                        for idx in tmp_deque:
                            arr[idx][0] = (x+d_x)
                            arr[idx][1] = (y+d_y)

                        if C[x+d_x][y+d_y] == 0:
                            chess[(x+d_x) * N + y + d_y+1].extend(tmp_deque)
                        elif C[x+d_x][y+d_y] == 1:
                            tmp_deque.reverse()
                            chess[(x+d_x) * N + y + d_y+1].extend(tmp_deque)

                        chess[(x) * N + y+1] = deque()

                        if len(chess[(x+d_x) * N + y + d_y+1]) >= 4:
                            flag = False
                            break

            else:
                d = reverse_dict[d]
                arr[i][2] = d
                d_x, d_y = direction_dict[d]
                if (0 <= x+d_x < N) and (0 <= y+d_y < N) and C[x+d_x][y+d_y] != 2:
                    tmp_deque = chess[(x) * N + y+1]
                    for idx in tmp_deque:
                        arr[idx][0] = (x+d_x)
                        arr[idx][1] = (y+d_y)

                    if C[x+d_x][y+d_y] == 0:
                        chess[(x+d_x) * N + y + d_y+1].extend(tmp_deque)
                    elif C[x+d_x][y+d_y] == 1:
                        tmp_deque.reverse()
                        chess[(x+d_x) * N + y + d_y+ 1].extend(tmp_deque)
                    chess[(x) * N + y +1] = deque()

                    if len(chess[(x+d_x) * N + y + d_y+1]) >= 4:
                        flag = False
                        break

    cnt += 1
    
    if not flag:
        break
    if cnt > 1000:
        break

if cnt > 1000:
    print(-1)
else:
    print(cnt)