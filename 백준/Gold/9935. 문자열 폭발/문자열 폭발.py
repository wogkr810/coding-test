s = input()
t = list(input())
len_t = len(t)

stack = []

for i in range(len(s)):
    stack.append(s[i])
    if stack[-len_t:] == t:
        for _ in range(len_t):
            stack.pop()

print('FRULA') if not stack else print(''.join(stack))

    