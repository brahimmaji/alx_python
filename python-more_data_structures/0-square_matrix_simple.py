# Write a function that computes the square value of all integers of a matrix

#def square_matrix_simple(matrix=[]):
#matrix is a 2 dimensional array
def square_matrix_simple(matrix=[]):
    matrix=[]
    for x in matrix:
        square_row =[ y**2 for y in x]
        matrix.append(square_row)
    return matrix


square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
