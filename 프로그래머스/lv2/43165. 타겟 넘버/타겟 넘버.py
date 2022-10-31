'''
1. 총 경우의 수(최대) : 2 ** 20 = 1,048,576(백만) <- (-,+) ** (숫자종류 : 2~20)  

2. 풀이
numbers = [1,2,3,4,5]
target = 3
abs_numbers = [[-1,1],[-2,2],[-3,3],[-4,4],[-5,5]]
idx = '1111' <- 초기화 '1' * len(numbers)  -> 11111 -> 11110 -> 11101 -> 11011 .....
cnt : 정답이 되는 방법의 개수
target_sum -> abs_numbers 리스트의 각 인덱스에 접근을 하되, int(idx[i])로 [-,+] 접근
            
            ex : idx = '11011' , numbers = [1,2,3,4,5] -> 1 + 2 - 3 + 4 + 5

target_sum이 target과 같다면 cnt += 1

3. 시간복잡도 : 
- len(numbers) = N 
-> O(1) : abs_numbers 생성
-> while문 경우의 수 : 2**20(백만) * ( N : sum 리스트 접근 + log(n) : bin + n : zfill)

--> 백만 * (2n + log(n)) 정도 일듯?

'''

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