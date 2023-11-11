from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline


N, K, R = map(int,input().split())
road = set()
for _ in range(R):
    a, b, c, d = list(map(int,input().split()))
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    road.add((a, b, c, d))
    road.add((c, d, a, b))

cow = []
for _ in range(K):
    tmp_input = list(map(int,input().split()))
    tmp_input = [i-1 for i in tmp_input]
    cow.append(tmp_input)


dxy = [[0,1], [0,-1], [1,0], [-1,0]]
cnt = 0

def is_inside(a, b, N):
    if (0 <= a < N) and (0 <= b < N):
        return True
    return False

for combination in combinations([i for i in range(K)], 2):
    s, e = cow[combination[0]], cow[combination[1]]
    visited = [[False] * N for _ in range(N)]

    q = deque([s])
    visited[s[0]][s[1]] = True 
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if is_inside(dx, dy, N):
                if not visited[dx][dy]:
                    if (x,y,dx,dy) not in road:
                        q.append([dx,dy])
                        visited[dx][dy] = True

    if not visited[e[0]][e[1]]:
        cnt += 1

print(cnt)