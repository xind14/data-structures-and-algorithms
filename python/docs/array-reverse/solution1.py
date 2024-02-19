def reverseArray(arr):

    start, end = 0, len(arr) - 1

    while start < end:

        arr[start], arr[end] = arr[end], arr[start]

        start += 1

        end -= 1

    return arr




# input_array = [1, 2, 3, 4, 5]

# result = reverseArray(input_array)

# print("Reversed Array:", result)