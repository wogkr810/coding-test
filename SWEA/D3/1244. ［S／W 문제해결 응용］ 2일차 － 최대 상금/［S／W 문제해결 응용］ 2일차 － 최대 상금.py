# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = input().split()
    arr = list(V)
    N = len(arr)
    cnt = 0
    ans = 0
    
    def dfs(idx, count):
        global ans
        if count == int(E):
            ans = max(int(''.join(arr)), ans)
            return
        for i in range(idx, N):
            for j in range(i+1, N):
                if arr[i] <= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    dfs(i, count+1)
                    arr[i], arr[j] = arr[j], arr[i]

        if not ans and count < int(E):
            flag = (int(E)-count) % 2
            if flag:
                arr[-1], arr[-2] = arr[-2], arr[-1]
            dfs(idx, int(E))

    dfs(0,0)
    print(f'#{tc} {ans}')


