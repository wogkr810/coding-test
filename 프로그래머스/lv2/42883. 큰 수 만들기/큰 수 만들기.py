def solution(number, k):
    stack = []
    c = k
    
    for num in number:
        if not stack:
            stack.append(num)
            continue
        
        if stack[-1] < num:
            while k and stack[-1] < num:
                stack.pop()
                k -= 1
                
                if not stack:
                    break
        stack.append(num)
              
    stack = stack[:-k] if k>0 else stack
    return ''.join(stack)
                
