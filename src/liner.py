from fractions import Fraction

LIMIT = 10

def row_plus_times(matrix):
    while 1:
        try:
            num1, num2, z = map(int, input("rowA rowB x: ").split())
            break
        except:
            print("error")
    
    num1 -= 1
    num2 -= 1

    rowA = matrix[num1]
    rowB = list(map(lambda n: n*z, matrix[num2]))

    matrix[num1] = list(map(lambda x, y: x+y, rowA, rowB))

    print("")
    for i in matrix:
        for j in i:
            print(Fraction(str(j)).limit_denominator(LIMIT), end=', ')
        print("")
    print("")

def row_plus_division(matrix):
    while 1:
         try:
             num1, num2, z = map(int, input("rowA rowB x: ").split())
             break
         except:
             print("error")
     
    num1 -= 1
    num2 -= 1
 
    rowA = matrix[num1]
    rowB = list(map(lambda n: n/z, matrix[num2]))
 
    matrix[num1] = list(map(lambda x, y: x+y, rowA, rowB))
    
    print("")
    for i in matrix:
        for j in i:
            print(Fraction(str(j)).limit_denominator(LIMIT), end=', ')
        print("") 
    print("")

def row_times(matrix):
    while 1:
        try:
            num, z = map(int, input("row x: ").split())
            break
        except:
            print("error")

    num -= 1

    matrix[num] = list(map(lambda x: x*z, matrix[num]))

    print("")
    for i in matrix:
        for j in i:
            print(Fraction(str(j)).limit_denominator(LIMIT), end=', ')
        print("") 
    print("")

def row_division(matrix):
    while 1:
        try:
            num, z = map(int, input("row x: ").split())
            break
        except:
            print("error")

    num -= 1

    matrix[num] = list(map(lambda x: x/z, matrix[num]))

    print("")
    for i in matrix:
       for j in i:
           print(Fraction(str(j)).limit_denominator(LIMIT), end=', ')
       print("")  
    print("")

def row_plus_times_div(matrix):
    while 1:
        try:
            num1, num2, z, w = map(int, input("rowA rowB x y: ").split())
            break
        except:
            print("error")
    
    num1 -= 1
    num2 -= 1

    rowA = matrix[num1]
    rowB = list(map(lambda n: n*z/w, matrix[num2]))

    matrix[num1] = list(map(lambda x, y: x+y, rowA, rowB))

    print("")
    for i in matrix:
        for j in i:
            print(Fraction(str(j)).limit_denominator(LIMIT), end=', ')
        print("")
    print("") 

def row_swap(matrix):
    while 1:
        try:
            rowA, rowB = map(int, input("rowA rowB: ").split())
            break
        except:
            print("error")
    
    rowA -= 1
    rowB -= 1

    list = matrix[rowA]
    matrix[rowA] = matrix[rowB]
    matrix[rowB] = list

    print("")
    for i in matrix:
       for j in i:
           print(Fraction(str(j)).limit_denominator(LIMIT), end=', ')
       print("")
    print("")

def main():
    print("Let`s go! Liner Algebra!")
    while 1:
        try:
           rowNum = int(input("row number: ")) 
           break
        except:
            print("error")

    matrix = []

    for i in range(0,rowNum):
        while 1:
            try:
               list = [int(x) for x in input("row" + str(i+1) + " Items: ").split()] 
               break
            except:
                print("error")
                
        matrix.append(list)

    for i in matrix:
        print(i)

    while True:
        while 1:
            try:
                print("0 = row+row*x, 1 = row+row/x, 2 = row*x, 3 = row/x, 4 = row+row*x/y, 5 = swap, 6~ = exit")
                flag = int(input("number: "))
                break
            except:
                print("number only....")

        if flag == 0:
            row_plus_times(matrix)
        elif flag == 1:
            row_plus_division(matrix)
        elif flag == 2:
            row_times(matrix)
        elif flag == 3:
            row_division(matrix)
        elif flag == 4:
            row_plus_times_div(matrix)
        elif flag == 5:
            row_swap(matrix)
        else:
            break
    
    print("bye-bye")


if __name__=='__main__':
    main()