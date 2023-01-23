T = input() 
a_count = T.count('a')
len_t = len(T)
T = T*2
min_value = 1e5

for i in range(len_t):
    min_value = min(T[i:i+a_count].count('b'), min_value)

print(min_value)