import sys
A, B, C = map(int,sys.stdin.readline().split())

def power(a, b):
    if b == 1:
        return a % C
    else:
        x=power(a,b//2)
        if b % 2 == 0:
            return x * x % C
        
        else:
            return x * x * a % C

print(power(A,B))