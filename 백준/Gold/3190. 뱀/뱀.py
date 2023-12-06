from collections import deque

def is_inside(x,y):
    if (0 <= x < N) and (0 <= y < N):
        return True
    return False

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 1
L = int(input())
direction = [list(input().split()) for _ in range(L)]

dxy = [[0,1], [1,0], [0,-1], [-1,0]]
t = 0
d = 0
snake = deque([[0,0]])
x, y = 0, 0

while True:
    t += 1
    x += dxy[d][0]
    y += dxy[d][1]

    if [x,y] in snake or not is_inside(x,y):
        break

    if arr[x][y] == 1:
        arr[x][y] = 0
    else:
        snake.popleft()
    snake.append([x,y])
    
    if direction:
        if t == int(direction[0][0]):
            rt = direction[0][1]
            if rt == 'L':
                d = (d-1) % 4
            elif rt == 'D':
                d = (d+1) % 4
            direction.pop(0)

print(t)