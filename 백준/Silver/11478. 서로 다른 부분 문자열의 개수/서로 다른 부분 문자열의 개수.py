S=input()
hubo_set=set()
for i in range(len(S)):
    for j in range(1,len(S)+1):
        hubo_set.add(S[i:i+j])

print(len(hubo_set))