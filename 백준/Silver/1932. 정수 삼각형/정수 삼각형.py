N=int(input())
tri=[]
for i in range(N):
    arr=list(map(int,input().split()))
    tri.append(arr)

for i in range(1,len(tri)):
    for j in range(len(tri[i])):
        if j==0:
            tri[i][j]=tri[i-1][j]+tri[i][j]
        elif j==len(tri[i])-1:
            tri[i][j]=tri[i-1][j-1]+tri[i][j]
        else:
            tri[i][j]=max(tri[i-1][j-1],tri[i-1][j]) + tri[i][j]

print(max(tri[len(tri)-1]))