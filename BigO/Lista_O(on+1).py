# Não importa o tamanho dos dados sempre vamos retorna algo tipo, o Inicio da lista ou o fim, ou o meio 
def Frist_idx(data):
    return data[0]

data = [1,2,3,4,5,6,7,8,9,10]
print(Frist_idx(data))
# nesse exemplo chamamos uma O(n + 1)