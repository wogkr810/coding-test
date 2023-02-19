from copy import deepcopy
N = int(input())
s = list(map(int,input()))
f = list(map(int,input()))

for i in range(2):
    cnt = 0
    flag = True
    start = deepcopy(s)
    
    if i==1:
        cnt += 1 
        start[0] = (start[0]+1) % 2
        start[1] = (start[1]+1) % 2
    for j in range(1,N):
        if start[j-1] != f[j-1]:
            cnt += 1

            start[j-1] = (start[j-1]+1) % 2
            start[j] = (start[j]+1) % 2
            if j != N-1:
                start[j+1] = (start[j+1]+1) % 2

        if start == f:
            flag = False
            break
    
    if not flag:
        break
    
if not flag:
    print(cnt)
else:
    print(-1)
