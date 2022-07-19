import sys
import re

N=int(input())
ls=[]
for i in range(N):
    str_input=input()
    ls.append(str_input)


for j in range(len(ls)):
    for i in range(len(ls[j])-1):
        if ls[j][i]!=ls[j][i+1]:
            if ls[j][i+1] in ls[j][:i]:
                N-=1
                break

print(N)