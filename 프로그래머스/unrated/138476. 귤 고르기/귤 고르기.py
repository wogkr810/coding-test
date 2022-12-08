from collections import Counter,deque

def solution(k, tangerine):
    counter = Counter(tangerine)
    counter_sort = deque(sorted(counter.items(), key = lambda x : x[1] , reverse = True))
    cnt = 0

    while True:
        x,y = counter_sort.popleft()
        k -= y
        cnt += 1
        if k <= 0:
            break
    
    return cnt