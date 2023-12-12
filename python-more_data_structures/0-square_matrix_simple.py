def square_matrix_simple(matrix=[]):
    result = [[]]
    for row in matrix:
        for elem in row:
            squared_row = [elem ** 2]
            result.append(squared_row)
    return map(square_matrix_simple,result)

#matrix
matrix = [[]]
print(square_matrix_simple(matrix))
print(matrix)
