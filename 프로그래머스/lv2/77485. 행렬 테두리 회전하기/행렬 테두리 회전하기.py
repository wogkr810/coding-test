from collections import deque

def spiral_order(matrix):
    result = []
    while matrix:
        # 왼쪽에서 오른쪽으로 이동
        result += matrix[0]
        matrix = list(zip(*matrix[1:]))
        # 시계 반대 방향으로 90도 회전
        matrix = matrix[::-1]
    return result

def solution(rows, columns, queries):
    matrix = [[0] * columns for _ in range(rows)] 
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = (i) * columns  + (j+1)
    
    ans = []

    for query in queries:
        x1, y1, x2 , y2 = query
        res = []
        for i in range(x1,x2+1):
            tmp_res = []
            for j in range(y1,y2+1):
                tmp_res.append([i-1,j-1])
            res.append(tmp_res)

        spiral = deque(spiral_order(res))
        for _ in range((x2-x1-1) * (y2-y1-1)):
            spiral.pop()

        value_list = [matrix[a][b] for a,b in spiral]
        spiral.rotate(-1)
        min_value = int(1e10)

        for k in range(len(spiral)):
            min_value = min(min_value, value_list[k])
            x, y = spiral[k]
            matrix[x][y] = value_list[k]

        ans.append(min_value)

    return ans