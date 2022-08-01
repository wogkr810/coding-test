arr=[]
while True:
    text=input()
    if text=='.':
        break
    arr.append(text)

for i in range(len(arr)):
    text_list=[]
    for j in arr[i]:
        if j=="[" or j=="]" or j=="(" or j==")":
            text_list.append(j)
    text_list=''.join(text_list)
    len_text_list=len(text_list)
    cnt=0
    while cnt<len_text_list:
        cnt+=1
        text_list=text_list.replace("()","")
        text_list=text_list.replace("[]","")
    if len(text_list)>0:
        print("no")
    else:
        print("yes")