from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
people = defaultdict(str)

for _ in range(N):
    p, s = input().split()
    if p in people:
        if people[p] == 'enter' and s == 'leave':
            del people[p]
    else:
        if s == 'enter':
            people[p] = 'enter'

for _ in sorted(people.keys(), reverse = True):
    print(_)