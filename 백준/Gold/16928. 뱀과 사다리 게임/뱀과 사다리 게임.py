from collections import defaultdict, deque
N, M = map(int,input().split())

S, B = defaultdict(int), defaultdict(int)

for _ in range(N):
    a, b = map(int,input().split())
    S[a] = b

for _ in range(M):
    a, b = map(int,input().split())
    B[a] = b

visited = [False] * 101
board = [0] * 101
q = deque([1])
visited[1] = True

while q:
    x = q.popleft()

    if x == 100:
        break

    for i in range(1,7):
        dx = x + i
        if dx <= 100 and not visited[dx]:
            if dx in S:
                dx = S[dx]
            if dx in B:
                dx = B[dx]
            if not visited[dx]:
                q.append(dx)
                visited[dx] = True
                board[dx] = board[x] + 1


print(board[-1])