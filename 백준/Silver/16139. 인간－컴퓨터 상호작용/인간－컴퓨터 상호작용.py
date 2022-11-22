from collections import defaultdict
import sys
import string

S = list(sys.stdin.readline())
T = int(sys.stdin.readline())
idx_dict = {}

for s in string.ascii_lowercase:
    idx_dict[s] = [0]
    cnt = 0
    for i in range(len(S)):
        if S[i] == s:
            cnt += 1
        idx_dict[s].append(cnt)

for _ in range(T):
    x, y, z = sys.stdin.readline().split()
    (y,z) = (int(y), int(z))
    print(idx_dict[x][z+1] - idx_dict[x][y])
