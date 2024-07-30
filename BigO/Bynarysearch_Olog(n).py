
data = [1,2,3,4,5,6,7,8,9]

for idx in range(0, len(data),3):
    print(data[idx])

def Binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1 
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError ("Valor não esta na lista")

print(Binary_search(data, 8))
# nesse exemplo chamamos uma Olog(n)