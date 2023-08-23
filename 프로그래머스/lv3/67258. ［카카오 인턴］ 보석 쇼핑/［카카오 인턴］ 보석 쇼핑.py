from collections import defaultdict

def solution(gems):
    left, right = 0, 0
    gem_type = set(gems)
    len_gems = len(gem_type)
    gem_dict = defaultdict(int)
    gem_dict[gems[0]] = 1
    res = []

    while left < len(gems)  and  right < len(gems) :
        if len_gems == len(gem_dict):
            res.append([left + 1 , right + 1])
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]

            left += 1
        else:
            right += 1
            if right == len(gems):
                break
            gem_dict[gems[right]] += 1

    res.sort(key = lambda x : (x[1]-x[0]))
    return res[0]