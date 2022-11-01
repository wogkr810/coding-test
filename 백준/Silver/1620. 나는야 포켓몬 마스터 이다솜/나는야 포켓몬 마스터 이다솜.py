from collections import defaultdict

N, M = map(int,input().split())

poketmon_id = defaultdict()
poketmon_name = defaultdict()
result = []

for i in range(1,N+1):
    poketmon = input()
    poketmon_id[i] = poketmon
    poketmon_name[poketmon] = i

for _ in range(M):
    result.append(input())

for _ in result:
    if _.isdigit():
        print(poketmon_id[int(_)])
    else:
        print(poketmon_name[_])