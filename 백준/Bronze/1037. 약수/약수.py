N=int(input())
arr=list(map(int,input().split()))
arr.sort()

if len(arr)%2==1:
    print(arr[int(len(arr)/2)]**2)
else:
    print(arr[0]*arr[-1])