# Write a function that computes the square value of all integers of a matrix

#def square_matrix_simple(matrix=[]):
#matrix is a 2 dimensional array
def square_matrix_simple(matrix=[]):
    result=[]
    for x in matrix:
        square_row = []
        square_row =[ y**2 for y in x]
        matrix.append(square_row)
    return result
