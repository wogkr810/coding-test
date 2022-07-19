cro_alpha=["c=","c-","dz=","d-","lj","nj","s=","z="]

S=input()

count=0
while len(S)>=1:
    if S[:3] in cro_alpha:
        count+=1
        S=S[3:]
    elif S[:2] in cro_alpha:
        count+=1
        S=S[2:]
    else:
        S=S[1:]
        count+=1

print(count)