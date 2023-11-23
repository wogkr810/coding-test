T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int,input().split())

    ans = 0
    f = 0

    for i in range(a):
        p, q = divmod(b-f,c)
        if q == 0:
            ans += p
            f = 0
        elif q != 0:
            if i == a-1:
                ans -= 1
            ans += (p+2)
            f = (c-q)
    
    print(f'Case #{tc}: {ans}')