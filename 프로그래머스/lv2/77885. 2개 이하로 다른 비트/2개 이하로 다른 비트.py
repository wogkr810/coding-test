def solution(numbers):
    def change_bin(input):
        if input == '0':
            return '1'
        else:
            return '0'

    res = []
    for number in numbers:
        if number % 2 == 0:
            res.append(number+1)
        else:
            number_bin = ['0']+ list(bin(number)[2:])
            for i in range(len(number_bin)-1,-1,-1):
                if number_bin[i] == '0':
                    number_bin[i] = change_bin(number_bin[i])
                    number_bin[i+1] = change_bin(number_bin[i+1])
                    break
            res.append(int(''.join(number_bin),2))
            
    return res