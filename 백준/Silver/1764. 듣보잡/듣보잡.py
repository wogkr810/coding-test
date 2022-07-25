import sys

N,M=map(int,sys.stdin.readline().split())
arr1=[]
arr2=[]
for i in range(N):
    arr1.append(sys.stdin.readline().rstrip())
for i in range(M):
    arr2.append(sys.stdin.readline().rstrip())

inter=list(set(arr1).intersection(set(arr2)))
inter.sort()

print(len(inter))

for i in inter:
    print(i)