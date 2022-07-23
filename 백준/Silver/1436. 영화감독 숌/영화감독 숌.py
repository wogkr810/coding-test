N=int(input())
ls=[]
i=1
while True:
    i+=1
    if '666' in str(i):
        ls.append(i)
    if len(ls)==N:
        break
    
print(ls[-1])