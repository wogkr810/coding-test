import sys

N = int(sys.stdin.readline())
arr = []
x_list = []
y_list = []
z_list = []
for i in range(N):
    x, y, z = map(int,sys.stdin.readline().split())
    arr.append([i+1,x, y ,z])
    x_list.append([i+1,x])
    y_list.append([i+1,y])
    z_list.append([i+1,z])

x_list.sort(key=lambda x : x[1])
y_list.sort(key=lambda x : x[1])
z_list.sort(key=lambda x : x[1])

planet = []
for j in range(1,N):
    planet.append([x_list[j-1][0],x_list[j][0],abs(x_list[j-1][1]-x_list[j][1])])
    planet.append([y_list[j-1][0],y_list[j][0],abs(y_list[j-1][1]-y_list[j][1])])
    planet.append([z_list[j-1][0],z_list[j][0],abs(z_list[j-1][1]-z_list[j][1])])

planet.sort(key=lambda x: x[2])


parent = [i for i in range(N+1)]
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

cnt = 0
for i in planet:
    a, b, c = i
    if find_parent(parent,a) != find_parent(parent,b):
        cnt += c
        union(parent,a,b)

print(cnt)