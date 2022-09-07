import itertools

def solution(sizes):
    odd_even_sizes=list(itertools.chain.from_iterable(sizes))
    max_index=odd_even_sizes.index(max(odd_even_sizes))
    
    answer=0
    tmp=0
    if (max_index+1)%2==0:
        for i in range(len(sizes)):
            if sizes[i][1]>=sizes[i][0]:
                sizes[i][1]=tmp
                sizes[i][1]=sizes[i][0]
                sizes[i][0]=tmp
        right_index=[]
        for i in range(len(sizes)):
            right_index.append(sizes[i][1])
        answer=max(odd_even_sizes)*max(right_index)
    else:
        for i in range(len(sizes)):
            if sizes[i][0]>=sizes[i][1]:
                sizes[i][0]=tmp
                sizes[i][0]=sizes[i][1]
                sizes[i][1]=tmp
        left_index=[]
        for i in range(len(sizes)):
            left_index.append(sizes[i][0])
        answer=max(odd_even_sizes)*max(left_index)
    

    return answer