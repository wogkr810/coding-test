import sys
N=int(sys.stdin.readline().strip())
arr1=list(map(int,sys.stdin.readline().strip().split()))
M=int(sys.stdin.readline().strip())
arr2=list(map(int,sys.stdin.readline().strip().split()))

arr1.sort()

for i in arr2:
    start=0
    end=N-1
    while start<=end:
        mid=(start+end)//2
        if arr1[mid]==i:
            print(1)
            break
        elif arr1[mid]<i:
            start=mid+1
        else:
            end=mid-1
    else:
        print(0)