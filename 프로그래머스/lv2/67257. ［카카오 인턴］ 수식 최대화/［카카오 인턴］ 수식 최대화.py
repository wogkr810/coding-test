from itertools import permutations
import re

def operate(e,a,b):
    if e == '+':
        return a+b
    if e == '-':
        return a-b
    if e == '*':
        return a*b
def solution(expression):
    result = []
    s = []
    op_lists = list(permutations(['+','-','*'],3))
    expression = re.split("([^0-9])",expression)
    for op_list in op_lists:
        exp = expression
        for op in op_list:
            s = []
            for e in exp:
                if s and s[-1] == op:
                    operation = s.pop()
                    s[-1] = operate(operation,int(s[-1]),int(e))
                else:
                    s.append(e)
            exp = s
        result.append(abs(exp[0]))
    return max(result)