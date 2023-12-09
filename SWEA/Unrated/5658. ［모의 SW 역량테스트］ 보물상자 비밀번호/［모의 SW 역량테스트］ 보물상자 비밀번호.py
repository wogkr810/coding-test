# import sys

# sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    key = list(input())

    hubo = []
    for _ in range(N//4):
        for i in range(0, N, N//4):
            hubo.append(''.join(key[i:i+N//4]))
        now = key.pop()
        key = [now] + key


    print(f'#{tc} {int(sorted(set(hubo), reverse= True)[K-1],16)}')
