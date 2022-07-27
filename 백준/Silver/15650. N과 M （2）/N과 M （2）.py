N, M = map(int,input().split())

s=[]
visited=[False] * (N+1)

def check_incre(arr):
    if len(arr)==1:
        return True
    else:
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        else:
            return True

def dfs():
    if len(s)==M and check_incre(s):
        print(' '.join(map(str,s)))
        return
    for i in range(1,N+1):
        if visited[i] :
            continue
        visited[i]=True
        s.append(i)
        dfs()
        s.pop()
        visited[i]=False

dfs()