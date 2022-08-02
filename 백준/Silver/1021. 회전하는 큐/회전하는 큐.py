from collections import deque
N, M = map(int,input().split())
arr=deque([i for i in range(1,N+1)])
dq=deque(list(map(int,input().split())))

cnt=0

while len(dq)>0:
    if arr.index(dq[0])>len(arr)//2:
        cnt+=len(arr)-arr.index(dq[0])
        arr.rotate(len(arr)-arr.index(dq[0]))
        arr.popleft()
        dq.popleft()
    else:
        cnt+=arr.index(dq[0])
        arr.rotate(-arr.index(dq[0]))
        arr.popleft()
        dq.popleft()
print(cnt)