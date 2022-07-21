N=int(input())

fibo_list=[0,1]

for i in range(N-1):
    fibo_list.append(fibo_list[-1]+fibo_list[-2])

if N==0:
    print(0)
else:
    print(fibo_list[-1])