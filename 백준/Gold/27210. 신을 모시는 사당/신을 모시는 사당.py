N = int(input())
arr = list(map(int,input().split()))

sin_plus = [1 if i ==1 else -1 for i in arr]
sin_minus = [-1 if i ==1 else 1 for i in arr]
dp_plus = [sin_plus[0]] + [0] * (N-1)
dp_minus = [sin_minus[0]] + [0] * (N-1)
for i in range(1,N):
    dp_plus[i] = max(dp_plus[i],dp_plus[i-1]+sin_plus[i])
    dp_minus[i] = max(dp_minus[i],dp_minus[i-1]+sin_minus[i])


print(max(max(dp_plus),max(dp_minus)))