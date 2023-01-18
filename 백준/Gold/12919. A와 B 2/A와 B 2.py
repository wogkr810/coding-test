import sys
sys.setrecursionlimit(10**5)

S = input()
T = input()

ans = 0

def make_ab(start):
    global S, ans

    if len(start) == 0:
        return

    if start == S:
        ans = 1
        return

    if start[-1] == "A":
        make_ab(start[:-1])
    
    if start[0] == "B":
        make_ab(start[1:][::-1])


make_ab(T)
print(ans)
