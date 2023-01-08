import sys
N, M = map(int,sys.stdin.readline().rstrip().split())
word = set()
for _ in range(N):
    word.add(sys.stdin.readline().rstrip())

for _ in range(M):
    word -= set(sys.stdin.readline().rstrip().split(','))
    print(len(word))
