from collections import defaultdict  # <- Counter지우기
T = int(input())

for _ in range(T):
    N = int(input())
    fashion_dict = defaultdict(int)
    for i in range(N):
        dress, kind = input().split()        # <- type 예약어라 다른 걸로
        fashion_dict[kind] += 1
    res = 1
    for i in list(fashion_dict.values()):
        res = res *(i+1)
    print(res-1)