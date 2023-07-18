from collections import deque
from copy import deepcopy

def solution(key, lock):
    N, M = len(lock), len(key)

    arr = [[0] * (2*M +N -2) for _ in range(2*M +N -2)]
    
    for i in range(M-1, M+N-1):
        arr[i][M-1:M+N-1] = lock[i-M+1]

    def transpose_matrix(matrix):
        n = len(matrix)

        # 회전한 결과를 저장할 새로운 배열 생성
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[i][j] = matrix[j][i]

        return rotated
        
    def rotate_matrix(matrix):
        n = len(matrix)

        # 회전한 결과를 저장할 새로운 배열 생성
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]

        return rotated

    def is_locked(arr, N, M, x, y, key):
        for i in range(M):
            for j in range(M):
                    arr[x+i][y+j] += key[i][j]

        for i in range(M-1, M+N-1):
            for j in range(M-1, M+N-1):
                if arr[i][j] != 1:
                    return False
        return True

    rotated_keys = [key]
    for _ in range(3):
        rotated_keys.append(rotate_matrix(rotated_keys[-1]))
        
    # rotated_keys.append(transpose_matrix(key))
    # for _ in range(3):
    #     rotated_keys.append(rotate_matrix(rotated_keys[-1]))

    for r_k in rotated_keys:
        for row in range(N+M-1):
            for col in range(N+M-1):
                if is_locked(deepcopy(arr), N, M, row, col, r_k):
                    return True

    return False