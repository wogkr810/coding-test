def is_divide(arr1, arr2, divisor):
    for i in arr1:
        if i % divisor != 0:
            return False
    for j in arr2:
        if j % divisor == 0:
            return False
    return True     

def solution(arrayA, arrayB):
    ans = 0

    for i in range(2,10001):
        left, right = is_divide(arrayA, arrayB, i), is_divide(arrayB, arrayA, i)
        if (left and not right) or (right and not left):
            ans = i
    return ans