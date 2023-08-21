from collections import defaultdict
from itertools import product

def solution(user_id, banned_id):
    ban_dict = defaultdict(list)

    for idx, banner in enumerate(banned_id):
        for user in user_id:
            for i in range(min(len(banner),len(user))):
                if banner[i] != user[i] and banner[i] != '*':
                    break
            else:
                if len(banner) == len(user):
                    ban_dict[idx].append(user)

    N = len(ban_dict)
    res = []
    for hubo in list(product(*ban_dict.values())):
        tmp_set = set(hubo)
        if len(tmp_set) == N and tmp_set not in res:
            res.append(tmp_set)

    return len(res)
