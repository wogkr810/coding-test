R, C = map(int,input().split())
arr = []
for _ in range(R):
    arr.append(list(input()))

alpha_visit = [False] * 26

dxy = [[0,1],[0,-1],[1,0],[-1,0]]
res = 0
alpha_visit[ord(arr[0][0])-65] = True

def DFS(x,y,cnt):
    global res
    res = max(res,cnt)
    for i in range(4):
        dx = x + dxy[i][0]
        dy = y + dxy[i][1]
        if (0<=dx<R) and(0<=dy<C):
            if not alpha_visit[ord(arr[dx][dy])-65]:
                alpha_visit[ord(arr[dx][dy])-65] = True
                DFS(dx,dy,cnt+1)
                alpha_visit[ord(arr[dx][dy])-65] = False

DFS(0,0,1)
print(res)