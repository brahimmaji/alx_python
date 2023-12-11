#Write a function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print(y,end="")
    print()    


#You can assume that the list only contains integers
#You are not allowed to cast integers into strings
#You have to use str.format() to print integers
