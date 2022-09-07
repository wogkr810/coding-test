def solution(arr):
    jungbok_index_list=[]
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            jungbok_index_list.append(i)
    
    answer=[]
    bigyo=list(set([i for i in range(len(arr))])-set(jungbok_index_list))
    
    for i in bigyo:
        answer.append(arr[i])

    return answer