N=int(input())
arr=[list(input().split()) for i in range(N)]

for i in range(len(arr)):
    arr[i][0]=int(arr[i][0])

arr.sort(key=lambda x: x[0])

for i in range(len(arr)):
    print(arr[i][0],arr[i][1])