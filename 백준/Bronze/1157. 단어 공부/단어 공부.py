from collections import Counter

S=input()
count=Counter(S.lower()).most_common()

if len(count)==1:
    print(count[0][0].upper())
else:
    if count[0][1]==count[1][1]:
        print("?")
    else:
        print(count[0][0].upper())