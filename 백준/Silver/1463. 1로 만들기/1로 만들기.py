N=int(input())
arr=[0] * (1000001)
arr[0]=0
arr[1]=0
arr[2]=1
arr[3]=1

for i in range(4,len(arr)):
    hubo=[]
    if i%3==0:
        hubo.append(1+arr[int(i/3)])
    if i%2==0:
        hubo.append(1+arr[int(i/2)])
    hubo.append(1+arr[i-1])

    arr[i]=min(hubo)

print(arr[N])