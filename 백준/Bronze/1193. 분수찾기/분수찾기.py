N=int(input())
count=0
while N>0:
    count+=1
    N-=count
if count%2==1:
    print(f"{(1-N)}/{(count+N)}")
else:
    print(f"{(count+N)}/{(1-N)}")