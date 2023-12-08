from collections import Counter
from itertools import chain

r, c, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]


t = 0


def transpose(arr):
    n = len(arr)
    m = len(arr[0])
    transposed = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(arr[j][i])
        transposed.append(tmp)

    return transposed

def operation(arr):
    max_cnt = -1
    tmp_arr = []
    for i in range(len(arr)):
        counter = Counter(arr[i])
        if 0 in counter:
            del counter[0]
        counter = list(chain(*sorted(counter.items(), key = lambda x : (x[1],x[0]))))
        if len(counter) >= 100:
            counter = counter[:100]
        tmp_arr.append(counter)
        max_cnt = max(max_cnt, len(counter))
    for i in range(len(arr)):
        if len(tmp_arr[i]) < max_cnt:
            for _ in range(max_cnt- len(tmp_arr[i])):
                tmp_arr[i].append(0)
        arr[i] = tmp_arr[i]
    return arr


while True:
    try:
        if arr[r-1][c-1] == k:
            break
    except:
        pass
    
    if t >= 101:
        break
    t += 1

    n = len(arr)
    m = len(arr[0])

    if n >= m:
        arr = operation(arr)
    elif n < m:
        transposed_arr = transpose(arr)
        transposed_arr = operation(transposed_arr)
        arr = transpose(transposed_arr)


if t >= 101:
    print(-1)
else:
    print(t)
