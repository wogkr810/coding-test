def solution(n, m, puddles):
    arr = [[0] * m for _ in range(n)]

    puddles = [[puddle[0]-1,puddle[1]-1]for puddle in puddles]

    for i in range(n):
        if [i,0] in puddles:
            break
        arr[i][0] = 1

    for j in range(m):
        if [0,j] in puddles:
            break
        arr[0][j] = 1

    for i in range(1,n):
        for j in range(1,m):
            hubo = []
            if [i,j] in puddles:
                continue
            if [i-1,j] not in puddles:
                hubo.append(arr[i-1][j])
            if [i,j-1] not in puddles:
                hubo.append(arr[i][j-1])

            arr[i][j] = sum(hubo)
    return arr[n-1][m-1] % 1000000007