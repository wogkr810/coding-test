from collections import deque

A, B = map(int,input().split())

queue=deque([[A,1]])
while queue:
    tmp,cnt=queue.popleft()
    if tmp<B:
        queue.append([tmp*2,cnt+1])
        queue.append([10*tmp+1,cnt+1])
    if tmp==B:
        print(cnt)
        break
else:
    print(-1)