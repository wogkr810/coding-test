N=int(input())
arr=list(map(int,input().split()))

arr.sort()
acc_sum=[]

for i in range(len(arr)):
    acc_sum.append(sum(arr[:i+1]))

print(sum(acc_sum))