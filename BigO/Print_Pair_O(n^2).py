# Permutação:  Print os pares da sequencia de numeros
def Print_Pair(some_list):
    for i in some_list: #n
        for j in some_list: #n
            print("Item: {}, {}".format(i,j))

Print_Pair([1,2,3,4])
# nesse exemplo chamamos uma O(n^2)