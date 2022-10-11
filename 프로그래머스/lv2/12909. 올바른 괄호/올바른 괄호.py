from collections import deque

def solution(s):
    s= deque(list(s))
    stack = []
    while s:
        tmp = s.popleft()
        stack.append(tmp)
        if stack[-2:-1] == ["("]:
            if tmp == ")":
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False