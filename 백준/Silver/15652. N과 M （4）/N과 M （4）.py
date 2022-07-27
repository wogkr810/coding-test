N, M = map(int,input().split())

s=[]

def dfs(start):
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    for i in range(start,N+1):
        s.append(i)
        dfs(start)
        start+=1
        s.pop()

dfs(1)