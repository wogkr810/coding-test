def solution(records):
    records=list(map(lambda x : x.split(),records))

    final_dict=dict()
    for i in records:
        try:
            final_dict[i[1]]=i[2]
        except:
            pass

    for i in range(len(records)):
        if len(records[i])!=2:
            records[i][2]=final_dict[records[i][1]]
        else:
            records[i].append(final_dict[records[i][1]])

    res=[]
    for record in records:
        if record[0]=="Enter":
            res.append(f"{final_dict[record[1]]}님이 들어왔습니다.")
        elif record[0]=="Leave":
            res.append(f"{final_dict[record[1]]}님이 나갔습니다.")
        else:
            pass

    return res
    