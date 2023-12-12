
def square_matrix_simple(matrix=[]):
    result=[]
    for x in matrix:
        square_row = []
        square_row.append =[ y**2 for y in x]
        matrix.append(square_row)
    return result
#def square_matrix_simple(matrix=[]):
 

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    squared_matrix = square_matrix_simple(matrix)
    print(squared_matrix)
    print(matrix)


