from collections import defaultdict

N = int(input())
arr_dict = defaultdict()
for i in range(1,N+1):
    arr_dict[i] = int(input())

answer = set()

def dfs(start,set1,set2,visited):
    visited[start] = True
    set1.add(start)
    set2.add(arr_dict[start])
    if set1 == set2:
        answer.update(set1)
    else:
        if not visited[arr_dict[start]]:
            dfs(arr_dict[start],set1,set2,visited)

for i in range(1,N+1):
    if i not in answer:
        visited = [False] * (N+1)
        dfs(i,set(),set(),visited)

print(len(answer))
for _ in sorted(answer):
    print(_)