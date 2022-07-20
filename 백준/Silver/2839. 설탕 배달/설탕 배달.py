N=int(input())
res=[]
for i in range(int(N/5)+1):
    for j in range(int(N/3)+1):
        if 5*i+3*j==N:
            res.append(i+j)
if len(res)==0:
    print(-1)
else:
    print(min(res))