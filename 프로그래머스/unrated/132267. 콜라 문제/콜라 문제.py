def solution(a, b, n):
    res = 0
    while True:
        p,q = divmod(n,a)
        res += p*b
        n = n - p*a + p*b
        if n < a:
            break

    return res