from collections import deque

N, K = map(int,input().split())
arr = list(map(int,input().split()))
arr = deque([[arr[i],0] for i in range(2*N)])

cnt = 0

while True:

    nagu_cnt = 0
    cnt += 1

    #1
    arr.rotate(1)
    arr[N-1][1] = 0

    #2
    for i in range(N-2,0,-1):
        if arr[i+1][1] == 0 and arr[i+1][0] !=0 and arr[i][1] ==1 :
            arr[i][1] = 0
            arr[i+1][0] -= 1
            arr[i+1][1] = 1
    
    arr[N-1][1] = 0

    # 3
    if arr[0][0] != 0 and arr[0][1] !=1:
        arr[0][1] = 1
        arr[0][0] -=1


    #4
    for i in range(len(arr)):
        if arr[i][0] == 0:
            nagu_cnt += 1
    
    if nagu_cnt >= K:
        break
    

print(cnt)
    