def solution(answers):
    one_list=[1,2,3,4,5]
    two_list=[2,1,2,3,2,4,2,5]
    three_list=[3,3,1,1,2,2,4,4,5,5]
    c_1=0
    c_2=0
    c_3=0
    for i in range(len(answers)):
        if answers[i]==one_list[i%5]:
            c_1+=1
        if answers[i]==two_list[i%8]:
            c_2+=1
        if answers[i]==three_list[i%10]:
            c_3+=1   
    result=[c_1,c_2,c_3]
    mmaaxx=max(result)
    answer=[]
    if result.count(mmaaxx)==3:
        answer=[1,2,3]
    elif result.count(mmaaxx)==2:
        for i in range(3):
            if result[i]==mmaaxx:
                answer.append(i+1)
    elif result.count(mmaaxx)==1:
        for i in range(3):
            if result[i]==mmaaxx:
                answer.append(i+1)
    # print(answer)
    return answer