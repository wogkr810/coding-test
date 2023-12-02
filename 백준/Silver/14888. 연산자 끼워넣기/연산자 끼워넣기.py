from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
op = list(map(int,input().split()))

ops = []
for i in range(len(op)):
    ops.extend(str(i+1) * op[i])

min_value = int(1e10)
max_value = int(-1e10)

for perm in permutations(ops):
    ans = arr[0]
    for i in range(N-1):
        if perm[i] == '1':
            ans += arr[i+1]
        elif perm[i] == '2':
            ans -= arr[i+1]
        elif perm[i] == '3':
            ans *= arr[i+1]
        elif perm[i] == '4':
            if ans >= 0:
                ans //= arr[i+1]
            else:
                ans *= -1
                ans //= arr[i+1]
                ans *= -1

    min_value = min(min_value, ans)
    max_value = max(max_value, ans)

print(max_value)
print(min_value)
    