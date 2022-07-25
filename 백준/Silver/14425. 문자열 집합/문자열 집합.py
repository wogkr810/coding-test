import sys

N,M=map(int,sys.stdin.readline().split())
arr1=[]
arr2=[]
for i in range(N):
    arr1.append(input())
for j in range(M):
    arr2.append(input())

inter=set(arr1).intersection(set(arr2))

cnt=0

for i in arr2:
    if i in inter:
        cnt+=1
print(cnt)