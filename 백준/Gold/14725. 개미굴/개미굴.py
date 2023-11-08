N = int(input())
food = []
for _ in range(N):
    tmp_input = list(map(str,input().split()))
    food.append(tmp_input[1:])

food.sort()
ans = []

for i in range(N):
    if i == 0:
        for j in range(len(food[i])):
            ans.append('--' * j + food[i][j])
    else:
        idx = 0
        for j in range(len(food[i])):
            if food[i-1][j] != food[i][j] or len(food[i-1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(food[i])):
            ans.append('--' * j + food[i][j])

for _ in ans:
    print(_)
