# 3 Pessoas na Fila, quantas conbinações elas podem se organizar
def Permutation(data, n):
    if n == 1:
        print(data)
        return
    for i in range(n):
        Permutation(data, n-1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0],data[n-1] = data [n-1], data[0]

data = [1,2,3]
Permutation(data,len(data))
# nesse exemplo chamamos uma O(n!)