import re

def solution(dartResult):
    dartResult = re.sub('10','K',dartResult) 
    res = []
    stack = []
    for i in dartResult:
        if i.isdigit():
            stack.append(int(i))
        elif i == "K":
            stack.append(10)
        elif i in ["S", "D", "T"]:
            if i == "D":
                stack[-1] = stack[-1] * stack[-1]
            elif i == "T":
                stack[-1] = stack[-1] * stack[-1] * stack[-1]
        elif i == "*":
            for j in range(1,3):
                try:
                    stack[-j] *= 2
                except:
                    pass
        elif i == "#":
            stack[-1] *= -1

    return sum(stack)