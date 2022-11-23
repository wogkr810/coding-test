import sys
sys.setrecursionlimit(10000)

N = int(input())
arr = list(map(int,input().split()))
operations = list(map(int,input().split()))

add,sub,multi,divide = operations
min_value = 1e9
max_value = -1e9

def DFS(depth,value,add,sub,multi,divide):
    global min_value,max_value
    if depth == N-1:
        min_value = min(min_value,value)
        max_value = max(max_value,value)     
        return   
    if add:
        DFS(depth+1,value + arr[depth+1],add-1,sub,multi,divide)
    if sub:
        DFS(depth+1,value - arr[depth+1],add,sub-1,multi,divide)
    if multi:
        DFS(depth+1,value * arr[depth+1],add,sub,multi-1,divide)
    if divide:
        DFS(depth+1,int(value / arr[depth+1]),add,sub,multi,divide-1)


DFS(0,arr[0],add,sub,multi,divide)
print(max_value)
print(min_value)