N=int(input())

res=[]
for i in range(N):
    i=str(i)
    res.append(sum(map(int,list(i)))+int(i))

for i in range(len(res)):
    if res[i]==N:
        print(i)
        break
else:
    print(0)
    