S=input()
hubo_list=[]
for i in range(len(S)):
    for j in range(1,len(S)+1):
        hubo_list.append(S[i:i+j])

print(len(set(hubo_list)))