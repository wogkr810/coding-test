from collections import deque

def sep(string):
    u =''
    v =''
    l_cnt = 0
    r_cnt = 0
    for i in range(len(string)):
        if string[i] == '(':
            l_cnt += 1
        elif string[i] == ')':
            r_cnt += 1
        if l_cnt == r_cnt:
            u = ''.join(list(string)[:i+1])
            v = ''.join(list(string)[i+1:])
            break
    return u, v

def reverse_string(bracket):
    bra_dict = {'(' : ')', ')':'('}
    res = ''
    for i in bracket:
        res += bra_dict[i]
    return res
        

def check_bra(string):
    stack = deque()
    for i in string:
        if not stack:
            if i == ')':
                return False
            elif i == '(':
                stack.append(i)
        else:
            if stack[-1] == '(':
                if i == ')':
                    stack.pop()
                else:
                    stack.append(i)
    if not stack:
        return True
    else:
        return False
    


def solution(p):
    def bra(w):
        global ans
        ans = ''
        if not w:
            return ''

        u, v = sep(w)

        if check_bra(u):
            ans += u
            ans += bra(v)
        else:
            ans += '('
            ans += bra(v)
            ans += ')'
            ans += reverse_string(u[1:-1])

        return ans
    return bra(p)
