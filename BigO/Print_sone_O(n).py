# Usamos somente um for para printar os itens da lista
def Print_Item(data):
    for i in data:
        print(i)

Print_Item([1,2,3,4,5])
# nesse exemplo chamamos uma O(n)

#Busca Linear
def Linear_Search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Valor não encontrado na Lista')

data = [1,3,7,4,5,9,0,11]
print(Linear_Search(data,11))