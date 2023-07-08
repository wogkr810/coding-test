import sys

input = sys.stdin.readline

N = int(input())

plan = []
for i in range(1, N+1):
    plan.append([i] + list(map(int,input().split())))

x_list = sorted(plan, key = lambda x : x[1])
y_list = sorted(plan, key = lambda y : y[2])
z_list = sorted(plan, key = lambda z : z[3])

edges = set()
for i in range(N-1):
    edges.add((x_list[i][0], x_list[i+1][0], abs(x_list[i][1] - x_list[i+1][1])))
    edges.add((y_list[i][0], y_list[i+1][0], abs(y_list[i][2] - y_list[i+1][2])))
    edges.add((z_list[i][0], z_list[i+1][0], abs(z_list[i][3] - z_list[i+1][3])))

edges = sorted(edges, key = lambda x : x[2])

parent = [0] + [i for i in range(1,N+1)]

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

res = 0

for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)
