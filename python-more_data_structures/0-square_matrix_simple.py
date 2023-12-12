# Write a function that computes the square value of all integers of a matrix

#def square_matrix_simple(matrix=[]):
#matrix is a 2 dimensional array
def square_matrix_simple(matrix=[]):
    matrix=[]
    for x in matrix:
        for y in x :
         new_matrix=y**2
    return new_matrix
