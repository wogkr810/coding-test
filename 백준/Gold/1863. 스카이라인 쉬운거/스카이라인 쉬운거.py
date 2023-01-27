from collections import deque
N = int(input())
arr = deque()
for _ in range(N):
    arr.append(list(map(int,input().split())))

ans = 0
stack = []
for i in range(len(arr)):
    x, y = arr[i]
    while stack and stack[-1] > y:
        ans += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    stack.append(y)

while stack:
    if stack[-1] > 0:
        ans += 1
    stack.pop()

print(ans)