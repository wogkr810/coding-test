from collections import deque
N=int(input())

dq=deque()
for i in range(1,N+1):
    dq.append(i)


while True:
    if len(dq)==1:
        print(dq[0])
        break
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        break
    dq.rotate(-1)
    if len(dq)==1:
        print(dq[0])
        break