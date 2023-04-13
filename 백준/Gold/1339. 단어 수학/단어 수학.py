from collections import defaultdict

N = int(input())
arr = []
len_alpha = 0
alpha_set = set()
for _ in range(N):
    tmp_input = input()
    len_alpha = max(len_alpha, len(tmp_input))
    alpha_set.update(set(tmp_input))
    arr.append(tmp_input)

alpha_dict = defaultdict(int)

for i in range(len(arr)):
    arr[i] = arr[i].zfill(len_alpha)

for key in alpha_set:
    alpha_dict[key] = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == key:
                alpha_dict[key] += 10 ** (len_alpha-j)

max_num = 9
final_alpha_dict = defaultdict()
for alphabet,_ in sorted(alpha_dict.items(), key = lambda x : x[1], reverse = True):
    final_alpha_dict[alphabet] = str(max_num)
    max_num -= 1

final_alpha_dict['0'] = ''

res = 0
for i in range(len(arr)):
    tmp_string =''
    for j in range(len(arr[i])):
        tmp_string += final_alpha_dict[arr[i][j]]
    res += int(tmp_string)

    
print(res)