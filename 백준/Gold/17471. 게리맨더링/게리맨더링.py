from collections import deque
from itertools import combinations

N = int(input())
ingu = [0] + list(map(int,input().split()))
arr = [[] for _ in range(N+1)]
for i in range(N):
    arr[i+1].extend(list(map(int,input().split()))[1:])

sublists = []
num_set = set([i for i in range(1,N+1)])
for i in range(1,N-1):
    for combination in combinations([i for i in range(1, N+1)], i):
        tmp_list = []
        tmp_list.append(list(combination))
        tmp_list.append(list(set(num_set)-set(combination)))
        sublists.append(tmp_list)

def check(lst):
    q = deque()
    q.append(lst[0])
    visited = [0] * (N+1)
    visited[lst[0]] = 1
    while q:
        now = q.popleft()
        for v in arr[now]:
            if v in lst and visited[v] == 0:
                q.append(v)
                visited[v] = 1

    for vt in lst:
        if visited[vt] == 0:
            return False

    return True  


ans = int(1e10)
for sublist in sublists:
    a, b = sublist
    if check(a) and check(b):
        a_ingu = sum([ingu[i] for i in a])
        b_ingu = sum([ingu[j] for j in b])
        tmp_res = abs(a_ingu-b_ingu)
        ans = min(ans,tmp_res)

if not sublists:
    print(abs(ingu[-1]-ingu[1]))
else:
    if ans == int(1e10):
        print(-1)
    else:
        print(ans)