from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    cnt = 0
    
    while people:
        if people[-1] + people[0] > limit:
            people.pop()
        else:
            if len(people) > 1:
                people.popleft()
                people.pop()
            else:
                people.pop()
        cnt += 1


    return cnt