hex_dict = {"10":'A', "11":"B", "12":"C", "13":"D", "14":"E","15":"F"}

def make_k_jinsu(n,k):
    res = ''
    while n > 0:
        n, div = divmod(n,k)
        div = str(div)
        if div in hex_dict:
            div = hex_dict[div]
        res += str(div)
    return res[::-1]

def solution(n, t, m, p):
    res = '0'
    for i in range(1,1000*100):
        res += make_k_jinsu(i,n)
        if len(res) >= t*m:
            break
        
    ans = ''
    for i in range(p-1,t*m,m):
        ans += res[i]
        
    return ans