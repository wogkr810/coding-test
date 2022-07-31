N , K = map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
cnt=0
while K>1:
    for i in range(len(arr)-1,-1,-1):
        if K>=arr[i]:
            tmp=K//arr[i]
            K-=tmp*arr[i]
            cnt+=tmp

print(cnt)