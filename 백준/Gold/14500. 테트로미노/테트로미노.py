# TODO : 반복문 중첩 없애기
def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])

    trans = [[0 for row in range(row)] for col in range(col)]

    for i in range(row):
        for j in range(col):
            trans[j][i]=matrix[i][j]
    return trans

N, M = map(int,input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))

arr_trans = transpose(arr)

hubo = []

# 일자 블록 가로
for i in range(N):
    for j in range(M-3):
        hubo.append(sum(arr[i][j:j+4]))

# 일자 블록 세로
for i in range(M):
    for j in range(N-3):
        hubo.append(sum(arr_trans[i][j:j+4]))

# 네모
for i in range(N-1):
    for j in range(M-1):
        hubo.append(arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1])

# L자 -> 가로 1자에 위왼쪽, 위오른쪽 , 아래 왼쪽, 아래 오른쪽
for i in range(N):
    for j in range(M-2):
        tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        try:
            if i>=1:
                hubo.append(tmp + arr[i-1][j])
                hubo.append(tmp + arr[i-1][j+2])
        except:
            pass
            
        try:
            hubo.append(tmp + arr[i+1][j])
            hubo.append(tmp + arr[i+1][j+2])
        except:
            pass

# L자 -> 세로 1자에 왼쪽위, 오른쪽위 , 왼아래, 오른아래
for i in range(M):
    for j in range(N-2):
        tmp = arr_trans[i][j] + arr_trans[i][j+1] + arr_trans[i][j+2]
        try:
            if i>=1:
                hubo.append(tmp + arr_trans[i-1][j])
                hubo.append(tmp + arr_trans[i-1][j+2])
        except:
            pass
            
        try:
            hubo.append(tmp + arr_trans[i+1][j])
            hubo.append(tmp + arr_trans[i+1][j+2])
        except:
            pass

# z자 , 좌우대칭 , 원래거 , 원래거 좌우대칭
    
for i in range(N-1):
    for j in range(M-2):
        hubo.append(arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2])
        hubo.append(arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j] + arr[i][j+2])

for i in range(N-2):
    for j in range(M-1):
        hubo.append(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
        hubo.append(arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])

# ㅗ 모양 
# 가로일자 위아래
for i in range(N):
    for j in range(M-2):
        tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] 
        try:
            hubo.append(tmp + arr[i+1][j+1])
        except:
            pass
        try:
            if i>=1:
                hubo.append(tmp + arr[i-1][j+1])
        except:
            pass
# 세로일자 위아래
for i in range(M):
    for j in range(N-2):
        tmp = arr_trans[i][j] + arr_trans[i][j+1] + arr_trans[i][j+2] 
        try:
            hubo.append(tmp + arr_trans[i+1][j+1])
        except:
            pass
        try:
            if i>=1:
                hubo.append(tmp + arr_trans[i-1][j+1])
        except:
            pass

print(max(hubo))