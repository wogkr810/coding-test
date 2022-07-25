N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]

arr.sort(key=lambda x : (x[0],x[1]))

for i in range(len(arr)):
    print(arr[i][0],arr[i][1])