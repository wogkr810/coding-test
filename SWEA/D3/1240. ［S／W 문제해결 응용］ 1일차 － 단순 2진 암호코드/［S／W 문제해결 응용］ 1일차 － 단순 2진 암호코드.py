
# import sys
# sys.stdin = open('input.txt')


T = int(input())

password_dict = {'0001101' : '0', '0011001' : '1', '0010011' : '2',\
                 '0111101' : '3', '0100011' : '4', '0110001' : '5', \
                    '0101111' : '6', '0111011' : '7', '0110111' : '8',\
                        '0001011' : '9'}

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        if '1' in arr[i]:
            s = arr[i].index('1')
            e = M - arr[i][::-1].index('1')
            idx = i
            break

    passwords = ''.join(arr[idx][s:e]).zfill(56)
    ans = []
    for i in range(0,56,7):
        ans.append(int(password_dict[passwords[i:i+7]]))

    odd = 0
    even = 0
    for i in range(len(ans)):
        if i % 2 != 0:
            even += ans[i]
        else:
            odd += 3 * ans[i]
    
    if (odd + even) % 10 == 0:
        print(f'#{tc} {sum(ans)}')
    else: 
        print(f'#{tc} 0')

