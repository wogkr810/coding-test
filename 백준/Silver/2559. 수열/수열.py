import sys

N , K = map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
pre_sum=[]
k_sum=sum(arr[:K])
pre_sum.append(k_sum)

for i in range(N-K):
    k_sum=k_sum+arr[i+K]-arr[i]    
    pre_sum.append(k_sum)

print(max(pre_sum))