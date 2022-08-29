N, M = map(int, input().split())
arr = list(map(int,input().split()))

cnt = 0
end = 0
tmp_sum=0

for i in range(N):
    while end < N and tmp_sum < M :
        tmp_sum += arr[end]
        end+=1
    if tmp_sum == M :
        cnt+=1
    tmp_sum -= arr[i]

print(cnt)