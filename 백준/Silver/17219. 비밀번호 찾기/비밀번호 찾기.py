from collections import defaultdict

N, M = map(int,input().split())

id=defaultdict(str)
for _ in range(N):
    site , password = input().split()
    id[site]=password

for _ in range(M):
    q=input()
    print(id[q])