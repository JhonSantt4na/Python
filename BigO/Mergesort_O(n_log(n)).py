# Organiza os numeros em ordem numerica
def Merge_Sort(data):
    if len(data) <=1:
        return
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    Merge_Sort(left_data)
    Merge_Sort(right_data)

    left_index = 0
    right_index = 0
    data_index = 0
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index +=1
        data_index += 1

    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]

data = [9,0,8,6,2,5,7,3,4,1]
Merge_Sort(data)
print(data)
# nesse exemplo chamamos uma O(n log n)