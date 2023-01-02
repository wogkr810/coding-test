import re

def solution(x):
    bin_count = 0
    zero_count = 0 

    while True:
        if x == '1':
            break
        zero_count += x.count('0')
        x = re.sub('0','',x)

        x = bin(len(x))[2:]
        bin_count += 1

    return [bin_count,zero_count]