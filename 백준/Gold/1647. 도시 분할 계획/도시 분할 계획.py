import sys
N, M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,sys.stdin.readline().split())))

parent_table = [0] + [i for i in range(1,N+1)]


def find_parent(parent_table,node):
    if parent_table[node] != node:
        parent_table[node] = find_parent(parent_table, parent_table[node])
    return parent_table[node]
        
def union_parent(parent_table,x,y):
    x = find_parent(parent_table , x)
    y = find_parent(parent_table , y)
    if x < y:
        parent_table[y] = x
    else:
        parent_table[x] = y

arr.sort(key = lambda x :x[2])

cnt = 0
line_cnt = 0
for i in range(len(arr)):
    if find_parent(parent_table,arr[i][0]) != find_parent(parent_table,arr[i][1]):
        line_cnt += 1
        if line_cnt <= (N-2):
            cnt += arr[i][2]
        union_parent(parent_table,arr[i][0],arr[i][1])

print(cnt)
