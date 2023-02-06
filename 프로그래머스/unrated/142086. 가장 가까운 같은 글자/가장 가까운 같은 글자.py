from collections import defaultdict

def solution(s):
    where_dict = defaultdict(list)
    res = []

    for i in range(len(s)):
        if where_dict[s[i]]:
            res.append(i-where_dict[s[i]][-1])
        else:
            res.append(-1) 
        where_dict[s[i]].append(i)
                                
    return res