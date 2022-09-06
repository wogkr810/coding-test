from collections import defaultdict

def solution(survey, choices):

    character = ["R", "T", "C", "F", "J", "M", "A", "N"]

    character_dict = defaultdict(int)

    for i in character:
        character_dict[i]

    for i in range(len(survey)):
        if choices[i] <= 3:
            character_dict[survey[i][0]] += (4-choices[i])
        elif choices[i] >= 5:
            character_dict[survey[i][1]] += (choices[i]-4)
        else:
            pass


    res = ''
    if character_dict["R"] >= character_dict["T"]:
        res += "R"
    else:
        res += "T"
    if character_dict["C"] >= character_dict["F"]:
        res += "C"
    else:
        res += "F"
    if character_dict["J"] >= character_dict["M"]:
        res += "J"
    else:
        res += "M"
    if character_dict["A"] >= character_dict["N"]:
        res += "A"
    else:
        res += "N"

    return res