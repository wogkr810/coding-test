from collections import deque

def is_correct(input):
    stack = []
    input = deque(input)
    while input:
        tmp = input.popleft()
        if not stack:
            if tmp in ["]", "}", ")"]:
                return False
            stack.append(tmp)
        else:
            if stack[-1] == '[':
                if tmp == "]":
                    stack.pop()
                else:
                    stack.append(tmp)
            elif stack[-1] == '{':
                if tmp == "}":
                    stack.pop()
                else:
                    stack.append(tmp)
            elif stack[-1] == "(":
                if tmp == ")":
                    stack.pop()
                else:
                    stack.append(tmp)
    
    if len(stack) != 0:
        return False
    else:
        return True


def solution(s):
    s = deque(s)
    cnt = 0
    s_count = 0

    while True:
        s_count += 1
        s.append(s.popleft())
        if is_correct(s):
            cnt += 1

        if s_count == len(s):
            break

    return cnt