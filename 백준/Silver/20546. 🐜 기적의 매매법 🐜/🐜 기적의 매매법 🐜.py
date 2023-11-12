money = int(input())
stocks = list(map(int,input().split()))

jh_money, jh_stock = money, 0
sm_money, sm_stock = money, 0
up, down = 0,0

for i in range(len(stocks)):
    a, jh_money = divmod(jh_money,stocks[i])
    jh_stock += a

    if stocks[i] > stocks[i-1]:
        up += 1
        down = 0
    elif stocks[i] < stocks[i-1]:
        down += 1
        up = 0
    else:
        up = 0
        down = 0
    
    if up >= 3:
        sm_money += sm_stock * stocks[i]
        sm_stock = 0
        up = 0
    elif down >= 3:
        c, sm_money = divmod(sm_money, stocks[i])
        sm_stock += c
        down = 0
  

jh_ans = jh_money + jh_stock * stocks[-1]
sm_ans = sm_money + sm_stock * stocks[-1]

if jh_ans > sm_ans:
    print('BNP')
elif jh_ans < sm_ans:
    print('TIMING')
else:
    print('SAMESAME')
    
