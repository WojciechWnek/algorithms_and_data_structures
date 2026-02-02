def selection_sort(list):
  sorted_list = []

  while len(list):
    lowest_index = 0

    for i in range(len(list) - 1):
      if list[lowest_index] > list[i]:
        lowest_index = i

    sorted_list.append(list[lowest_index])
    list.pop(lowest_index)    

  return sorted_list
    

list = [5, 8, 1, 4, 7]
result = selection_sort(list)
print(result)

