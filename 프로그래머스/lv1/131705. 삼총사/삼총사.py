from itertools import combinations

def solution(number):
    answer = 0
    number.sort()
    
    for combination in combinations(number,3):
        if sum(combination) == 0:
            answer += 1
    
    return answer