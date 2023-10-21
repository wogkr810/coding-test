def solution(arrayA, arrayB):
    answer = 0
    if len(arrayA) == 1:
        if arrayA[0] == arrayB[0]:
            return 0
        else:
            return max(arrayA[0], arrayB[0])
    else:
        m1 = 0
        m2 = 0
        gcd1 = gcd(arrayA[0], arrayA[1])
        gcd2 = gcd(arrayB[0], arrayB[1])
        answer = max(m1,m2)
        for i in range(2, len(arrayA)):
            gcd1 = gcd(gcd1, arrayA[i])
            gcd2 = gcd(gcd2, arrayB[i])
        if gcd1 != 1 and canDivide(arrayB, gcd1) == False:
                m1 = gcd1
        if gcd2 != 1 and canDivide(arrayA, gcd2) == False:
                m2 = gcd2
        answer = max(m1,m2)
    return answer

def gcd(a, b):
    
    if b == 0:
        return a
    else:
        if a < b:
            return gcd(a, b % a)
        else:
            return gcd(b, a % b)
        
def canDivide(array, a):
    for i in range(len(array)):
        if array[i] % a == 0:
            return True
    return False