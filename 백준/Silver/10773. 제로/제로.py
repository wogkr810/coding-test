N=int(input())
arr=[]

for i in range(N):
    arr.append(int(input()))

hubo=[]

for i in range(N):
    if arr[i]!=0:
        hubo.append(arr[i])
    else:
        hubo.pop(-1)
print(sum(hubo))