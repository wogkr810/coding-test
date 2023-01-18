import string
from collections import defaultdict

T = int(input())

for _ in range(T):
    w = input()
    K = int(input())
    alpha_dict = defaultdict(list)

    for lowercase in string.ascii_lowercase:
        alpha_dict[lowercase] = []


        for i in range(len(w)):
            if w[i] == lowercase:
                alpha_dict[lowercase].append(i)
                

    alpha_dict

    min_value, max_value = 1e5, 0

    for key,value in alpha_dict.items():
        for i in range(len(value)-K+1):
            min_value = min(min_value,value[i+K-1]-value[i]+1)
            max_value = max(max_value,value[i+K-1]-value[i]+1)

    if min_value == 1e5 or max_value == 0:
        print(-1)
    else:
        print(min_value,max_value)

