def solution(s):
    s = s[1:-1].split('},{')
    s[0] = s[0][1:]
    s[-1] = s[-1][:-1]
    s = sorted(s , key = lambda x : len(x))

    res = [int(s[0])]
    for i in range(1,len(s)):
        res.append(int((set(s[i].split(','))-set(s[i-1].split(','))).pop()))
        
    return res