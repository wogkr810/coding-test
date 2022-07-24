import sys
from collections import Counter

N=int(input())
a=[int(sys.stdin.readline().strip()) for i in range(N)]

a.sort()

counter=Counter(a).most_common()

print(round(sum(a)/len(a)))

if len(a)%2==0:
    print((a[int(len(a)//2)-1]+a[int(len(a)//2)])/2)
else:
    print(a[int(len(a)//2)])

if len(counter)==1:
    print(counter[0][0])
else:
    if counter[0][1]==counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])

print(max(a)-min(a))