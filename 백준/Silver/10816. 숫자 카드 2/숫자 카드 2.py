import sys

N=int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))

dt={}
for i in arr2:
    dt[i]=0

for i in arr1:
    try:
        dt[i]+=1
    except:
        pass

for i in range(len(arr2)):
    print(dt[arr2[i]],end=" ")