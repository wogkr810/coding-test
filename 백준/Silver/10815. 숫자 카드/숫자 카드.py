import sys

N=int(sys.stdin.readline())
arr1=set(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))
inter=arr1.intersection(set(arr2))

for i in arr2:
    if i in inter:
        print(1,end=" ")
    else:
        print(0,end=" ")