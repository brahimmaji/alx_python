#Write a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    matrix=[[]]
    for x in matrix :
        for y in x :
            new_matrix = y**y
            matrix=new_matrix.append()
    return new_matrix
matrix=[1,2,3]
print(square_matrix_simple(matrix))
