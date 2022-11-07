from collections import deque
from itertools import combinations
import copy
import sys


dxy = [[-1,0],[1,0],[0,-1],[0,1]]

def safe_count(arr):
    safe_cnt = 0
    for i in range(len(arr)):
        safe_cnt += arr[i].count(0)
    return safe_cnt


def bfs(graph):
    queue = deque()
    tmp_arr = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 2:
                queue.append([i,j])
    
    while queue:
        x, y = queue.popleft()
        for k in range(len(dxy)):
            dx = x + dxy[k][0]
            dy = y + dxy[k][1]
            if (0 <= dx< N) and (0 <= dy < M):
                if tmp_arr[dx][dy] == 0:
                    tmp_arr[dx][dy] = 2
                    queue.append([dx,dy])
    return tmp_arr

N, M = map(int,sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

hubo = []
zero_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_list.append([i,j])

for combination in combinations(zero_list,3):
    tmp_graph = copy.deepcopy(arr)
    for idx in combination:
        tmp_graph[idx[0]][idx[1]] = 1
    hubo.append(safe_count(bfs(tmp_graph)))

print(max(hubo))

