N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

for i in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            tmp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=tmp
    


for i in range(len(arr)):
    print(arr[i])