from collections import Counter

def solution(X, Y):
    xcnt = Counter(X)
    ycnt = Counter(Y)
    xycnt = list((xcnt & ycnt).elements())
    
    if not xycnt:
        return "-1"
    elif set(xycnt) == set(['0']):
        return '0'
    else:
        return ''.join(sorted(xycnt, reverse = True))
        
                