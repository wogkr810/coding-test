from copy import deepcopy
from collections import defaultdict

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def rotate_by_90deg(matrix):
    n = len(matrix) # 행
    m = len(matrix[0]) # 열
    
    new_matrix = [[0] * n for _ in range(m)] # 회전시킨 2차원배열 초기화
    
    for i in range(n):
    	for j in range(m):
        	new_matrix[j][n-i-1] = matrix[i][j]
			    
    return new_matrix

directions = defaultdict(list)
directions[0] = [0,1]
directions[1] = [-1,0]
directions[2] = [0,-1]
directions[3] = [1,0]
board = [[0] * 101 for _ in range(101)]
boards = []

for _ in arr:
    tmp_board = deepcopy(board)
    y, x, d, g = _
    dx, dy = x + directions[d][0], y + directions[d][1]
    tmp_board[x][y] = 1
    tmp_board[dx][dy] = 3
    final_x, final_y = dx, dy
    xy_list = [[x,y], [dx,dy]]

    while g:
        rotate_board = rotate_by_90deg(tmp_board)
        for i in range(101):
            for j in range(101):
                if rotate_board[i][j] == 3:
                    diff_x, diff_y = (final_x -i), (final_y -j)

        for i in range(101):
            for j in range(101):
                if rotate_board[i][j] in [2,3]:
                    tmp_board[i+diff_x][j+diff_y] = 2
                    xy_list.append([i+diff_x,j+diff_y])
                elif rotate_board[i][j] == 1:
                    tmp_board[i+diff_x][j+diff_y] = 3
                    final_x, final_y = i+diff_x, j+diff_y 
                    xy_list.append([i+diff_x,j+diff_y])

        g -= 1
    
    boards.append(tmp_board)

for bd in boards:
    for i in range(101):
        for j in range(101):
            board[i][j] += bd[i][j]

cnt = 0

for i in range(100):
    for j in range(100):
        if board[i][j] != 0 and board[i+1][j]!=0 and board[i][j+1]!=0 and board[i+1][j+1] != 0:
            cnt += 1

print(cnt)