from collections import deque

def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][i] = list_2d[i][j]
    return new

def solution(board, moves):
    crane = []
    
    moves = list(map(lambda x : len(board)-x , moves))
    moves = deque(moves)
    
    board = rotate_2d(board)
    
    cnt = 0
    
    while moves:
        flag = False
        tmp = moves.popleft()
        for i in range(len(board[tmp])):
            if board[tmp][i] != 0 :
                flag =True 
                crane.append(board[tmp][i])
                board[tmp][i] = 0
                break
        if flag:
            if [crane[-1:]] == [crane[-2:-1]]:
                cnt += 2
                crane = crane[:-2]
            
    return cnt
    