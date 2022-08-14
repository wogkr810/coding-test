from collections import defaultdict, deque
import sys

N ,M = map(int,sys.stdin.readline().split())

arr=[]
G=defaultdict(list)
visited=[False]*(N+1)
for _ in range(M):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in arr:
    G[i[0]].append(i[1])
    G[i[1]].append(i[0])

cnt=0


for i in range(1,len(visited)):
    if not visited[i]:
        queue=deque([i])
        while queue:
            tmp=queue.popleft()
            visited[tmp]=True
            for e in G[tmp]:
                if not visited[e]:
                    queue.append(e)
                    visited[e]=True
        cnt+=1

print(cnt)