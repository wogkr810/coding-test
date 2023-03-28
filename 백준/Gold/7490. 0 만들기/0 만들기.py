from itertools import product

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [i for i in range(2,N+1)]
    res = []
    for operation in product(['+','-',' '],repeat = N-1):
        tmp_str = '1'
        for j in range(len(operation)):
            if operation[j] == '+':
                tmp_str += '+' + str(arr[j]) 
            elif operation[j] == '-':
                tmp_str += '-' + str(arr[j])
            elif operation[j] == ' ':
                tmp_str += ' ' + str(arr[j])
        if eval(tmp_str.replace(' ','')) == 0:
            res.append(tmp_str)
    res.sort()
    for ans in res:
        print(ans)
    print(' ')
        