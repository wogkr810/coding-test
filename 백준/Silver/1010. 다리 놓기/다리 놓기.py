import math

N=int(input())
for i in range(N):
    a, b = map(int,input().split())
    print(math.factorial(b)//(math.factorial(b-a)*math.factorial(a)))