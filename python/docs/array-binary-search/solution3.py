def binary_search(arr, key):
  left = 0
  right = len(arr) - 1
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] == key:
          return mid
      elif arr[mid] < key:
          left = mid + 1
      else:
          right = mid - 1
  return -1


# arr = [1, 2, 3, 4, 5]
# key = 4
# expected_result = 3
# result = binary_search(arr, key)
# assert result == expected_result, f"Expected {expected_result}, but got {result}"
# print (result)