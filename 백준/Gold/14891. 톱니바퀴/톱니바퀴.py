from collections import deque

one = deque(input())
two = deque(input())
three = deque(input())
four = deque(input())

K = int(input())
arr = [list(map(int,input().split())) for _ in range(K)]

for _ in range(K):
    num, d = arr[_]
    o = one[2]
    t_1, t_2 = two[6], two[2]
    th_1, th_2 = three[6], three[2]
    f = four[6]

    if num == 1:
        one.rotate(d)
        if o != t_1:
            two.rotate(-1 * d)
            if t_2 != th_1:
                three.rotate(d)
                if th_2 != f:
                    four.rotate(-1*d)
    elif num == 2:
        two.rotate(d)
        if t_1!= o:
            one.rotate(-1 * d)
        if t_2!= th_1:
            three.rotate(-1 * d)
            if th_2 != f:
                four.rotate(d)
    elif num == 3:
        three.rotate(d)
        if th_2!= f:
            four.rotate(-1 * d)
        if th_1!= t_2:
            two.rotate(-1 * d)
            if t_1 != o:
                one.rotate(d)
    elif num == 4:
        four.rotate(d)
        if f != th_2:
            three.rotate(-1 * d)
            if th_1 != t_2:
                two.rotate(d)
                if t_1 != o:
                    one.rotate(-1*d)
    
cnt = 0
if one[0] == '1':
    cnt += 1
if two[0] == '1':
    cnt += 2
if three[0] == '1':
    cnt += 4
if four[0] == '1':
    cnt += 8

print(cnt)
