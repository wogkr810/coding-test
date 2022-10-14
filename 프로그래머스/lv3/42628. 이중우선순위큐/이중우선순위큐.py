from collections import deque

def solution(operations):
    ans = []
    for operation in operations:
        command , num = operation.split()
        num = int(num)
        if command == "I":
            ans.append(num)
            ans = deque(sorted(ans))
        elif command == "D":
            try:
                if num == -1:
                    ans.popleft()
                elif num == 1:
                    ans.pop()
            except:
                pass

    if len(ans) == 0:
        return [0,0]
    else:
        return [max(ans),min(ans)]