N = int(input())
arr = list(map(int,input().split()))
arr = [[arr[i],i+1] for i in range(N)]

res = [0] * N
stack = []

for i in range(len(arr)):
    while stack:
        if stack[-1][0] < arr[i][0]:
            stack.pop()
        else:
            res[i] = stack[-1][1]
            break
    stack.append(arr[i])

print(*res)