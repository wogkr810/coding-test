N, B = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

def mat_mul(arr1,arr2):
    mat=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sum=0
            for k in range(N):
                sum+=arr1[i][k]*arr2[k][j]
            mat[i][j]=sum%1000
    return mat

def mat_mul_mod(arr1,arr2,power):
    if power==1:
        return arr1
    else:
        x=mat_mul_mod(arr1,arr2,power//2)
        if power%2==0:
            return mat_mul(x,x)
        else:
            return mat_mul(arr1,mat_mul(x,x))

res= mat_mul_mod(arr,arr,B)
for i in range(len(res)):
    for j in range(len(res)):
        res[i][j]%=1000
    
for i in res:
    print(*i)