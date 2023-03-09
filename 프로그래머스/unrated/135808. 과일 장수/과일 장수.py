from collections import deque

def solution(k, m, score):
    score = deque(sorted(score,reverse=True))
    new_score = [] 
    while score:
        tmp_list = []
        for i in range(m):
            if score:
                tmp_list.append(score.popleft())
            else:
                break
        new_score.append(tmp_list)
        
    ans = 0
    for ns in new_score:
        if len(ns) == m:
            ans += ns[-1] * m
    return ans
