def row_sums(matrix):
    final_sums = []
    for row in matrix:
        row_sum = 0
        for value in row:
            row_sum += value if value is not None else 0
        final_sums.append(row_sum)
    return final_sums
    
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = row_sums(matrix)
# print(result)