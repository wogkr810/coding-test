from collections import deque,Counter

def solution(want, number, discount):
    want_list = []
    for i in range(len(number)):
        for j in range(number[i]):
            want_list.append(want[i])
    
    count_want = Counter(want_list)
    res = 0
    
    while True:
        if Counter(discount[:10]) == count_want:
            res += 1
        if len(discount) == 10:
            break
        discount.pop(0)
        
    return res