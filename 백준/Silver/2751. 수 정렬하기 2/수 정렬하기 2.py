import sys

N=int(sys.stdin.readline())
arr=[int(sys.stdin.readline().strip()) for i in range(N)]

arr.sort()
    
for i in range(len(arr)):
    print(arr[i])