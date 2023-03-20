def three_check(arr):
    res = []
    if arr[0] == arr[1] == arr[2]:
        if arr[0] != '.':
            res.append(arr[0])
    if arr[3] == arr[4] == arr[5]:
        if arr[3] != '.':
            res.append(arr[3])
    if arr[6] == arr[7] == arr[8]:
        if arr[6] != '.':
            res.append(arr[6])
    if arr[0] == arr[3] == arr[6]:
        if arr[0] != '.':
            res.append(arr[0])
    if arr[1] == arr[4] == arr[7]:
        if arr[1] != '.':
            res.append(arr[1])
    if arr[2] == arr[5] == arr[8]:
        if arr[2] != '.':
            res.append(arr[2])
    if arr[0] == arr[4] == arr[8]:
        if arr[0] != '.':
            res.append(arr[0])
    if arr[2] == arr[4] == arr[6]:
        if arr[2] != '.':
            res.append(arr[2])
    return res

while True:
    hubo = input()
    if hubo =="end":
        break
    res = three_check(hubo)
    xcnt = hubo.count('X')
    ocnt = hubo.count('O')

    if 'X' in res and 'O' in res:
        print('invalid')
    elif 'X' in res:
        if xcnt == ocnt + 1:
            print('valid')
        else:
            print('invalid')
    elif 'O' in res:
        if xcnt == ocnt:
            print('valid')
        else:
            print('invalid')
    else:
        if (xcnt,ocnt) == (5,4):
            print('valid')
        else:
            print('invalid')
