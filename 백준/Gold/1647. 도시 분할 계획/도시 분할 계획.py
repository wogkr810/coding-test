import sys
input = sys.stdin.readline

N, M = map(int,input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] + [i for i in range(1, N+1)]
edges = []
res = 0

for _ in range(M):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost , a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        last = cost

print(res - last)
