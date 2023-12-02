def comb(arr, k):
    n = len(arr)
    res = []

    if k > n:
        return res
    
    if k == 1:
        for i in arr:
            res.append([i])
    
    elif k > 1:
        for i in range(n-k+1):
            for j in comb(arr[i+1:], k-1):
                res.append([arr[i]]+j)

    return res


N = int(input())
arr = [[i] + list(map(int,input().split())) for i in range(N)]

ans = -1

for i in range(1, N+1):
    tmp_res = comb(arr, i)
    for j in tmp_res:
        value = 0
        s = 0
        for k in range(len(j)):
            if j[k][0] >= s:
                if (j[k][0] + j[k][1]) <= N:
                    value += j[k][2]
                    s = (j[k][1] + j[k][0])
            else:
                break
        
        ans = max(ans, value)
print(ans)