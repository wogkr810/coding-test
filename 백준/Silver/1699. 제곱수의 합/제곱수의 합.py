import sys
N = int(sys.stdin.readline())
dp_table = [i for i in range(N+1)]      

for i in range(1,N+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp_table[i] > dp_table[i-j*j] +1:
            dp_table[i] = dp_table[i-j*j] +1

print(dp_table[N])