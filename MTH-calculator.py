import math

def linearAlgebra():
    print("Enter a matrix row by row. Type 'done' when finished")
    matrix = []

    while True:
        row = input().split()
        if row[0] == "done":
            break
        for i in range(len(row)):
            row[i] = int(row[i])
            
        matrix.append(row)

    def options():
        print("What would you like to do?")
        print("a) Calculate determinant of 2x2 matrix")
        print("b) Calculate determinant of 3x3 matrix")
        option = input()
    
        if option == 'a':
            checkSquare(matrix)
            print(determinant3x3(matrix))

        if option == 'b':
            checkSquare(matrix)
            print(determinant2x2(matrix))

    def determinant2x2(matrix):
        return (matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1])

    def determinant3x3(matrix):
        return ((matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][1]*matrix[1][2]*matrix[2][0] + matrix[0][2]*matrix[1][0]*matrix[2][1]) -
                (matrix[2][0]*matrix[1][1]*matrix[0][2] + matrix[2][1]*matrix[1][2]*matrix[0][0] + matrix[2][2]*matrix[1][0]*matrix[0][1]))
        
    def determinantOfNxN(matrix):
        print("determinant algorithm under progress")
        #here come the calculations

    def checkSquare(matrix):
        if len(matrix) != len(matrix[0]):
            print("Can only find determinant of square matrix!")
            options() #either call this function or main function if reset is desired

    options()

linearAlgebra()

def calculus()
