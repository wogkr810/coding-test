from copy import deepcopy

N, M = map(int,input().split())
T = set(list(map(int,input().split()))[1:])
arr = [set(list(map(int,input().split()))[1:]) for _ in range(M)]


while True:
    tmp_T = deepcopy(T)
    for i in range(len(arr)):
        if arr[i].intersection(T):
            T.update(arr[i])
    if tmp_T == T:
        break

cnt = M
for i in range(len(arr)):
    if arr[i].intersection(T):
        cnt -= 1

print(cnt)