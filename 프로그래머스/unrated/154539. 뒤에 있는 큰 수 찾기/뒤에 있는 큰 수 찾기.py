def solution(numbers):
    ans = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            ans[stack.pop()] = numbers[i]
        stack.append(i)
        
    return ans