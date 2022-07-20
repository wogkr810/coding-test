bn_list=aa=[[0 for i in range(15)] for j in range(15)]
for i in range(len(bn_list)):
    bn_list[0][i]=i+1

for i in range(1,len(bn_list)):
    for j in range(len(bn_list)):
        for k in range(j+1):
            bn_list[i][j]+=int(bn_list[i-1][k])

T=int(input())
for i in range(T):
    n=int(input())
    k=int(input())
    print(int(bn_list[n][k-1]))