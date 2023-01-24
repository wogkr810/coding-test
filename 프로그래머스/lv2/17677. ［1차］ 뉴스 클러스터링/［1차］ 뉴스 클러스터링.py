import re
from copy import deepcopy

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    p = re.compile('[a-zA-Z]{2}')
    str1_set = []
    str2_set = []

    for i in range(len(str1)-1):
        tmp_regex = p.findall(''.join([str1[i],str1[i+1]]))
        if len(tmp_regex) != 0:
            str1_set.append(tmp_regex.pop())

    for j in range(len(str2)-1):
        tmp_regex = p.findall(''.join([str2[j],str2[j+1]]))
        if len(tmp_regex) != 0:
            str2_set.append(tmp_regex.pop())

    # 다중합집합
    str1_temp = str1_set.copy()
    str1_result = str1_set.copy()

    for i in str2_set:
        if i not in str1_temp:
            str1_result.append(i)
        else:
            str1_temp.remove(i)
    # 다중교집합
    result = []

    for i in str2_set:
        if i in str1_set:
            str1_set.remove(i)
            result.append(i)
            
    if len(str1_set) == 0 and len(str2_set) == 0:
        return 65536
    else:
        return int(len(result)/len(str1_result)*65536)
            