from collections import defaultdict
import string

def solution(msg):
    cnt = 0
    msg_dict = defaultdict()

    for alphabet in string.ascii_uppercase:
        cnt += 1
        msg_dict[alphabet] = cnt
        
    res = []
    start, end = 0,len(msg)

    while start < end:
        for j in range(end,0,-1):
            tmp_msg = msg[start:j]
            if tmp_msg in msg_dict.keys():
                res.append(msg_dict[tmp_msg])
                if j != end:
                    if (tmp_msg + msg[j]) not in msg_dict.keys():
                        cnt += 1
                        msg_dict[tmp_msg + msg[j]] = cnt
                break

        start += len(tmp_msg)
        
    return res