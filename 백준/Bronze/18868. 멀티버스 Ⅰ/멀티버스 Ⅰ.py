from itertools import combinations

M, N = map(int,input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))

cnt = 0
idx = [i for i in range(M)]
idx_N = [i for i in range(N)]
for combination in combinations(idx,2):
    flag = True
    x,y = combination
    A = arr[x]
    B = arr[y]
    for combi in combinations(idx_N,2):
        a,b = combi
        if (A[a] < A[b]) and (B[a] < B[b]):
            pass
        elif (A[a] == A[b]) and (B[a] == B[b]):
            pass
        elif (A[a] > A[b]) and (B[a] > B[b]):
            pass
        else:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)