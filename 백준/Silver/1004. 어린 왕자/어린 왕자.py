T=int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    N=int(input())
    arr=[]
    for i in range(N):
        arr.append(list(map(int,input().split())))

    cnt=0
    for i in range(len(arr)):
        d_start=((arr[i][0]-x1)**2+(arr[i][1]-y1)**2)**0.5
        d_end=((arr[i][0]-x2)**2+(arr[i][1]-y2)**2)**0.5
        if arr[i][2]>d_start and arr[i][2]<d_end: 
            cnt+=1
        elif arr[i][2]<d_start and arr[i][2]>d_end:
            cnt+=1    
    print(cnt)