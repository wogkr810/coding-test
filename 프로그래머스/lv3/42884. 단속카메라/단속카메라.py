from collections import deque

def solution(routes):
    routes.sort(key = lambda x : x[1])
    routes = deque(routes)
    first = routes.popleft()[1]
    cnt = 1

    while routes:
        tmp = routes.popleft()
        if tmp[0] <= first <= tmp[1]:
            continue
        else:
            routes.appendleft(tmp)
            first = tmp[1]
            cnt += 1
            
    return cnt