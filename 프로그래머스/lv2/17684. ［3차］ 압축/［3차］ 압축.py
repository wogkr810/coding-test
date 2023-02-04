from collections import defaultdict
import string

def solution(msg):
    cnt = 0
    msg_dict = defaultdict()

    for alphabet in string.ascii_uppercase:
        cnt += 1
        msg_dict[cnt] = alphabet
        
    msg = list(msg)
    res = []

    while msg:
        flag = True

        for j in range(len(msg),0,-1):
            if not flag:
                break
            tmp_msg = ''.join(msg[:j])
            for key,value in msg_dict.items():
                if tmp_msg == value:
                    res.append(key)
                    flag = False
                    if j != len(msg):
                        if (tmp_msg + msg[j]) not in msg_dict.values():
                            cnt += 1
                            msg_dict[cnt] = tmp_msg + msg[j]
                    break

        for _ in range(len(tmp_msg)):
            msg.pop(0)

    return res