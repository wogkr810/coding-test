from itertools import accumulate
import sys
M, N = map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
acc_sum=list(accumulate(arr))
for i in range(N):
    a , b = map(int,sys.stdin.readline().split())
    if a==b:
        print(arr[a-1])
    elif a==1:
        print(acc_sum[b-1])
    else:
        print(acc_sum[b-1]-acc_sum[a-2])