def solution(numbers, target):
    abs_numbers = [[-numbers[i],numbers[i]] for i in range(len(numbers))]

    idx = '1' * len(numbers)
    cnt = 0
    while True:
        target_sum = sum([abs_numbers[i][int(idx[i])] for i in range(len(numbers))])
        if target_sum == target:
            cnt += 1
        idx = bin(int(idx,2) -1)[2:].zfill(len(numbers))
        if idx == '0' * len(numbers):
            break
    
    return cnt