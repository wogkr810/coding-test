import sys

K, L = map(int,sys.stdin.readline().split())
arr = dict()
for i in range(L):
    sugang = sys.stdin.readline().rstrip()
    arr[sugang] = i 

arr = sorted(arr.items(),key = lambda x : x[1])

hubo_count = len(arr) if len(arr) < K else K

for j in range(hubo_count):
    print(arr[j][0])
