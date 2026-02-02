def quicksort(values):
  if len(values) <= 1:
    return values
  
  pivot = values[0]
  less = []
  more = []

  for value in values[1:]:
    if value <= pivot:
      less.append(value)
    else:
      more.append(value)

  return quicksort(less) + [pivot] + quicksort(more)
 
  
list = [5, 8, 1, 4, 7]
result = quicksort(list)
print(result)


