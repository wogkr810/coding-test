N=int(input())
arr=list(map(int,input().split()))
reverse=arr[::-1]

dp_left=[1 for _ in range(N)]
dp_right=[1 for _ in range(N)]


for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            dp_left[i]=max(dp_left[i],dp_left[j]+1)
        if reverse[i]>reverse[j]:
            dp_right[i]=max(dp_right[i],dp_right[j]+1)

dp_right.reverse()

hubo=[]

for i in range(N):
    hubo.append(dp_left[i]+dp_right[i])

print(max(hubo)-1)