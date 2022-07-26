def gcd(x,y):
    while y>0:
        x,y = y, x%y
    return x

N, M = map(int,input().split())

print(gcd(N,M))
print(int(N*M/gcd(N,M)))