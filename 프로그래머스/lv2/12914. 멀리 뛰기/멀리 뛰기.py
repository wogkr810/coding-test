def solution(n):
    pascal = [[0] * (n+2) for _ in range(n+2)]
    pascal[0][0] = 1
    pascal[1][0] = 1
    pascal[1][1] = 1

    for i in range(2,n+1):
        for j in range(n+1):
            if j ==0:
                pascal[i][j] = 1
            elif j == (n+1):
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    cnt = 0
    k = 0

    while True:
        cnt += pascal[n][k] 


        n -= 1
        k += 1

        if n < 1:
            break
    return cnt %1234567