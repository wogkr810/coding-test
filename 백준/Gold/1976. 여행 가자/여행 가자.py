N = int(input())
M = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
plan = list(map(int,input().split()))

plan = [plan[i]-1 for i in range(M)]

def dfs(start):
    if not visited[start]:
        visited[start] = True
        for i in range(N):
            if arr[start][i]:
                dfs(i)

visited = [False] * N
dfs(plan[0])


for i in range(len(plan)):
    if not visited[plan[i]]:
        print("NO")
        break
else:
    print("YES")
