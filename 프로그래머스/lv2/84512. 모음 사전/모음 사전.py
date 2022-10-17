from itertools import product

def solution(word):
    collection = ['A','E','I','O','U']

    collection_list = []

    for i in range(5):
        for pd in list(product(collection,repeat=i+1)):
            collection_list.append(''.join(pd))

    collection_list.sort()

    return collection_list.index(word)+1