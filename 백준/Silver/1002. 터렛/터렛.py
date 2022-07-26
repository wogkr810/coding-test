N=int(input())
for i in range(N):
    arr=list(map(int,input().split()))
    d=((arr[0]-arr[3])**2+(arr[1]-arr[4])**2)**0.5
    if d==0 and arr[2]==arr[5]:
        print(-1)
    elif (arr[2]+arr[5])>d and abs(arr[2]-arr[5])<d:
        print(2)
    elif (arr[2]+arr[5])==d or abs(arr[5]-arr[2])==d:
        print(1)
    elif (arr[2]+arr[5])<d or abs(arr[2]-arr[5])>d:
        print(0)