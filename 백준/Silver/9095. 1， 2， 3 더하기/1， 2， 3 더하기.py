from collections import deque

T=int(input())

for _ in range(T):
    q=int(input())
    queue=deque([q])
    cnt=0
    while queue:
        tmp=queue.popleft()
        if tmp>=3:
            queue.append(tmp-3)
        if tmp>=2:
            queue.append(tmp-2)
        if tmp>=1:
            queue.append(tmp-1)
        if tmp==0:
            cnt+=1
    print(cnt)