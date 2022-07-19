from collections import defaultdict

a=defaultdict(list)
a[2]=["A","B","C"]
a[3]=["D","E","F"]
a[4]=["G","H","I"]
a[5]=["J","K","L"]
a[6]=["M","N","O"]
a[7]=["P","Q","R","S"]
a[8]=["T","U","V"]
a[9]=["W","X","Y","Z"]

S=input()
res=0
for i in range(len(S)):
    for key,value in a.items():
        if S[i] in value:
            res+=int(key)

res+=len(S)
print(res)
