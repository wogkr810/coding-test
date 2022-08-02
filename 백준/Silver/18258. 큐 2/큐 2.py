import sys
from collections import deque

N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(sys.stdin.readline().split())

int_deque=deque()

for i in range(len(arr)):
    if arr[i][0]=='push':
        int_deque.appendleft(int(arr[i][1]))        
    elif arr[i][0]=='pop':
        if len(int_deque)==0:
            print(-1)
        else:
            print(int_deque.pop())
    elif arr[i][0]=='size':
        print(len(int_deque))
    elif arr[i][0]=='empty':
        if len(int_deque)==0:
            print(1)
        else:
            print(0)
    elif arr[i][0]=='front':
        if len(int_deque)==0:
            print(-1)
        else:
            print(int_deque[-1])
    elif arr[i][0]=='back':
        if len(int_deque)==0:
            print(-1)
        else:
            print(int_deque[0])
