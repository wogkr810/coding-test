from collections import defaultdict

N = int(input())
M = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
plan = list(map(int,input().split()))
plan = [plan[i]-1 for i in range(M)]

graph = defaultdict(list)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            graph[i].append(j)

parent = [i for i in range(N)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(N):
    for v in graph[i]:
        union_parent(parent,i,v)

for j in range(M-1):
    if parent[plan[j]] != parent[plan[j+1]]:
        print("NO")
        break
else:
    print("YES")