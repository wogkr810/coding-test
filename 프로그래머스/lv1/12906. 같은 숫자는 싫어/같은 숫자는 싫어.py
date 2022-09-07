from collections import deque

def solution(arr):
    res = []
    arr = deque(arr)
    while arr:
        tmp = arr.popleft()
        if len(res) == 0:
            res.append(tmp)
        elif tmp != res[-1]:
            res.append(tmp)
    
    return res
        