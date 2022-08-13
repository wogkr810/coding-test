S=input()
ans=input()

cnt=0
while True:
    tmp=S.find(ans)
    if tmp==-1:
        break
    cnt+=1
    S=S[:tmp]+'0'*len(ans)+S[tmp+len(ans):]

print(cnt)