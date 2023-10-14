from collections import defaultdict
from itertools import product
from copy import deepcopy

N, M = map(int,input().split())

left, right, up, down = [0,-1], [0, 1], [-1,0], [1,0]
cctv_dict = defaultdict(list)
cctv_dict[1] = [[left], [right], [up], [down]]
cctv_dict[2] = [[left,right], [up,down]]
cctv_dict[3] = [[left,up], [up,right], [right,down], [left,down]]
cctv_dict[4] = [[left,up,down], [left,up,right], [left,down,right], [up,down,right]]
cctv_dict[5] = [[left,down,up,right]]

cctv_xy = []
cctv_list = []
wall_xy = []

arr = []

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(M):
        if tmp[j] == 6:
            wall_xy.append([i,j])
        elif tmp[j] == 1:
            cctv_xy.append([1,i,j])
            cctv_list.append([i for i in range(4)])
        elif tmp[j] == 2:
            cctv_xy.append([2,i,j])
            cctv_list.append([i for i in range(2)])
        elif tmp[j] == 3:
            cctv_xy.append([3,i,j])
            cctv_list.append([i for i in range(4)])
        elif tmp[j] == 4:
            cctv_xy.append([4,i,j])
            cctv_list.append([i for i in range(4)])
        elif tmp[j] == 5:
            cctv_xy.append([5,i,j])
            cctv_list.append([i for i in range(1)])
    arr.append(tmp)


ans = int(1e10)

for directions in product(*cctv_list):
    cnt = 0 

    tmp_arr = deepcopy(arr)
    for i in range(len(directions)):
        cur_cctvs = cctv_dict[cctv_xy[i][0]][directions[i]]
        x, y = cctv_xy[i][1], cctv_xy[i][2]
        for cur_cctv in cur_cctvs:
            if cur_cctv == [0,1]:
                for j in range(y+1,M):
                    if tmp_arr[x][j] != 6:
                        if tmp_arr[x][j] not in [1,2,3,4,5]:
                            tmp_arr[x][j] = -1
                    else:
                        break               
            elif cur_cctv == [0,-1]:
                for j in range(y-1,-1,-1):
                    if tmp_arr[x][j] != 6:
                        if tmp_arr[x][j] not in [1,2,3,4,5]:
                            tmp_arr[x][j] = -1
                    else:
                        break
            elif cur_cctv == [1,0]:
                for j in range(x+1,N):
                    if tmp_arr[j][y] != 6:
                        if tmp_arr[j][y] not in [1,2,3,4,5]:
                            tmp_arr[j][y] = -1
                    else:
                        break
            elif cur_cctv == [-1,0]:
                for j in range(x-1,-1,-1):
                    if tmp_arr[j][y] != 6:
                        if tmp_arr[j][y] not in [1,2,3,4,5]:
                            tmp_arr[j][y] = -1
                    else:
                        break
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 0:
                cnt += 1

    ans = min(ans,cnt)
    
print(ans)
          