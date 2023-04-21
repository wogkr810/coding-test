from collections import defaultdict

def solution(name, yearning, photo):
    yearn_dict = defaultdict()

    for i in range(len(name)):
        yearn_dict[name[i]] = yearning[i]

    res = []

    for i in range(len(photo)):
        ans = 0 
        for j in range(len(photo[i])):
            if photo[i][j] in yearn_dict.keys():
                ans += yearn_dict[photo[i][j]]
        res.append(ans)

    return res