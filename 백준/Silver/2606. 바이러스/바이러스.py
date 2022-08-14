from collections import defaultdict, deque

N = int(input())
M = int(input())

arr=[]
for _ in range(M):
    arr.append(list(map(int,input().split())))

G=defaultdict(list)
for i in range(1,N+1):
    G[i]

for i in arr:
    G[i[0]].append(i[1])
    G[i[1]].append(i[0])

queue=deque([1])
visited=[False]*(N+1)

while queue:
    tmp=queue.popleft()
    if not visited[tmp]:
        visited[tmp]=True
        queue.extend(G[tmp])


cnt=0
for i in range(len(visited)):
    if visited[i]:
        cnt+=1

print(cnt-1)