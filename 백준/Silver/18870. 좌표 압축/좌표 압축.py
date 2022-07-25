import sys

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

dt={}
for a,b in enumerate(sorted(set(arr))):
    dt[b]=a

for i in range(len(arr)):
    print(dt[arr[i]],end=" ")