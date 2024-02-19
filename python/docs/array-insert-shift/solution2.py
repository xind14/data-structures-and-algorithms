def insertShiftArray(array, value):

  array_middle = len(array) // 2
  left_array=array[:array_middle]
  right_array=array[array_middle:]
  newArray= left_array + [value] + right_array
  
  return newArray


# array = [1, 2, 3, 4]
# value = 5
# result = insertShiftArray(array, value)
# assert result == [1, 2, 5, 3, 4], f"Expected [1, 2, 5, 3, 4], but got {result}"
# print(result)