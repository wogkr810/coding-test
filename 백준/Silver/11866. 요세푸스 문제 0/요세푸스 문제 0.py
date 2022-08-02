from collections import deque

N, K=map(int,input().split())

res=[]
dq=deque()
for i in range(N):
    dq.append(i+1)

while len(dq)>0:
    dq.rotate(-K+1)
    res.append(str(dq.popleft()))

print("<"+', '.join(res)+">")
