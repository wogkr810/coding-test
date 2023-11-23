from collections import deque

N, X = map(int,input().split())
arr = deque(map(int,input().split()))

sub_arr = deque()
tmp_sum = 0

for _ in range(X):
    now = arr.popleft()
    tmp_sum += now
    sub_arr.append(now)

acc_arr = [tmp_sum]

while arr:
    now_1 = arr.popleft()
    now_2 = sub_arr.popleft()
    tmp_sum += (now_1 - now_2)
    acc_arr.append(tmp_sum)
    sub_arr.append(now_1)

max_value = max(acc_arr)
if max_value == 0:
    print('SAD')
else:
    print(max_value)
    print(acc_arr.count(max_value))