# Função que acha o menor valor em um array
def buscarmenor(arr):
   menor = arr[0]       # Salvamos o primeiro indice e valor como menor
   menor_indice = 0
   for i in range(1, len(arr)):  # Vamos rodar a lista toda acresentando 1 pois ja temos o primeiro indice
      if arr[i] < menor:   
         menor = arr[i]    # Se o próximo número do array for menor que o primeiro
         menor_indice = i  # Vamos salvar ele e seu índice
   return menor_indice     
# Por fim, retornamos o valor e o índice do menor número 

# Agora vamos organizar o array do menor para o maior
def ordenacaoSelecao(arr):
   novoArr = []      # Vamos criar um novo array vazio
   for i in range(len(arr)):  # Rodar todo o array
      menor = buscarmenor(arr)  # Vamos usar a nossa função de retornar o menor valor
      novoArr.append(arr.pop(menor)) # Vamos adicionar na nova lista e remover do array original (Fazendo até zerar o array)
   return novoArr

array = [10, 2, 45, 1, 78, 8]
print(ordenacaoSelecao(array))