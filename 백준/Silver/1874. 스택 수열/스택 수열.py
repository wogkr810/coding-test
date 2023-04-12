from collections import deque

N = int(input())
ans =  [int(input()) for _ in range(N)]

stack = []
arr = deque([i for i in range(1,N+1)])
res = []

for i in range(N):
    while arr:
        if stack and stack[-1] == ans[i]:
            stack.pop()
            res.append('-')
            break
        stack.append(arr.popleft())
        res.append('+')
    
    if stack and stack[-1] == ans[i]:
        stack.pop()
        res.append('-')

if stack:
    print('NO') 
else:
    for i in res:
        print(i)  
    
        
    