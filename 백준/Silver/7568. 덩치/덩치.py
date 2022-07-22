N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(len(arr)):
    count=N
    for j in range(len(arr)):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count-=1
    print(N-count+1)