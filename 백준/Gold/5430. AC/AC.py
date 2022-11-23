from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    cnt = 0
    flag = True
    command = list(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if N == 0:
        arr = deque([])
    for i in command:
        if i=="R":
            cnt += 1
        elif i=="D":
            if len(arr) == 0:
                print("error")
                flag = False
                break
            if cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    if cnt % 2 == 1:
        arr.reverse()
    if flag:
        print("[" + ",".join(list(arr)) + "]")