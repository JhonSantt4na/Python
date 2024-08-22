def buscabinaria(array, valor):
   baixo = 0
   alto = len(array) - 1
   while baixo <= alto:
      meio = (baixo + alto) // 2
      chute = array[meio]
      if chute == valor:
         return array[meio]
      if chute < valor:
         baixo = meio + 1
      else:
         alto = meio - 1
   return None

array = [1,2,3,4,5,6,7,8,9]
valor = 10

print(buscabinaria(array, valor))