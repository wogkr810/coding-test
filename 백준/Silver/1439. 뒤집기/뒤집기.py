from collections import deque

cnt = 0
x = deque(input())
flag = x[0]

while x:
    now = x.popleft()
    if now == flag:
        continue
    else:
        cnt += 1
        flag = now

if cnt % 2 ==0:
    print(cnt//2)
else:
    print(cnt//2 +1)
