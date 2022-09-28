V, E = map(int,input().split())
arr = []
for _ in range(E):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : x[2])

parent = [i for i in range(V+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent, x , y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)
    if x < y :
        parent[y] = x
    else:
        parent[x] = y

cnt = 0
for i in range(len(arr)):
    a, b, c = arr[i]
    if find_parent(parent,a) != find_parent(parent, b):
        cnt += c
        union(parent, a, b)

print(cnt)