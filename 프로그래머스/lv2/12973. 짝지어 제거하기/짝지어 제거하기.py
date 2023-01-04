

def solution(s):
    stack = []
    s = list(s)
    stack.append(s.pop())

    while s:
        tmp = s.pop()
        if stack:
            if stack[-1] == tmp:
                stack.pop()
            else:
                stack.append(tmp)
        else:
            stack.append(tmp)  

    if stack:
        return 0
    else:
        return 1  
