from collections import deque

def solution(cards1, cards2, goal):
    result = "Yes"
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        tmp_goal = goal.popleft()
        if cards1 and tmp_goal == cards1[0]:
            cards1.popleft()
        elif cards2 and tmp_goal == cards2[0]:
            cards2.popleft()
        else:
            return 'No'
    return result