N, M = map(int, input().split())
arr1=[]
for i in range(N):
    arr1.append(list(map(int,input().split())))
M, K = map(int, input().split())
arr2=[]
for i in range(M):
    arr2.append(list(map(int,input().split())))

mat_mul=[]
for i in range(N):
    res=[]
    for j in range(K):
        sum=0
        for k in range(M):
            sum+=arr1[i][k]*arr2[k][j]
        res.append(sum)
    mat_mul.append(res)

for i in mat_mul:
    print(*i)
