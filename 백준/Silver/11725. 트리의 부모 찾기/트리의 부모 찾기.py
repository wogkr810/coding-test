from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
parents = [0] * (N+1)

def DFS(start,grpah,parents):
    for i in graph[start]:
        if parents[i] ==0:
            parents[i] = start
            DFS(i,graph,parents)

DFS(1,graph,parents)

for parent in parents[2:]:
    print(parent)
        
