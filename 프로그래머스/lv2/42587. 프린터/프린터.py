from collections import deque

def solution(priorities, location):
    priorities=deque(priorities)
    location_list=deque([i for i in range(len(priorities))])

    cnt=0

    while priorities:
        cnt+=1
        max_tmp=priorities.index(max(priorities))
        priorities.rotate(-max_tmp)
        location_list.rotate(-max_tmp)
        pr=priorities.popleft()
        lo=location_list.popleft()

        if lo==location:
            return cnt
            break