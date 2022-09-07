def solution(answers):
    len_ans = len(answers)
    
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5]
    
    div_one = divmod(len_ans,len(one))
    div_two = divmod(len_ans,len(two))
    div_three = divmod(len_ans,len(three))
    
    one_list = one * div_one[0] + one[:div_one[1]]
    two_list = two * div_two[0] + two[:div_two[1]]
    three_list = three * div_three[0] + three[:div_three[1]]
    
    res = {1:0 , 2:0 , 3:0}
    
    for i in range(len(answers)):
        if answers[i] == one_list[i]:
            res[1] += 1
        if answers[i] == two_list[i]:
            res[2] += 1
        if answers[i] == three_list[i]:
            res[3] += 1
    
    res = sorted(res.items(), key = lambda x : x[1], reverse=True)
    
    return [i[0] for i in res if i[1]==res[0][1]]