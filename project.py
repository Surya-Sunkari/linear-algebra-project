# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:13:04 2022

@author: 100031985
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


"""
Things it can do right now:
    2d vector grapher
    determinant calculator (no plotting)
    matrix-matrix and scalar-matrix matrix multiplication
    calculate transpose of matrix
    find the normal equation for doing linear regression
    
Additions?:
    simple 2d vector grapher
    determinant calculator for 2d and 3d matrices (should plot determinant for 2d matrices)
    transformation calculator and viewer for 2d matrices
    inverse calculator (!!!)
    calculate lin reg using inverses
    calculate lin reg into fractions instead of decimal
"""

def get_vectors_2d():
    vectors = []
    
    while True:
        kb = input('Enter a 2d vector separated by a space, or "done" when finished:  ')
        if kb == 'done':
            break
        kb = kb.split()
        try:
            vectors.append([int(kb[0]), int(kb[1])])
        except:
            print('Problem with your input. Make sure to follow the "x y" format.')
        else:
            print('Vector successfully appended.')
    
    return vectors

def vector_grapher_2d():
    M = np.array(get_vectors_2d())
    colors = list(mcolors.BASE_COLORS)
    
    print('\nNow graphing:\n', M)
    
    rows,cols = M.T.shape
    
    # get absolute maxes for axis ranges to center origin, adds buffer space
    maxes = 1.1*np.amax(M, axis = 0)
    mins = 1.1*np.amin(M, axis=0)
    
    for i,l in enumerate(range(0,cols)):
        #xs = [0,M[i,0]]
        #ys = [0,M[i,1]]
        #plt.plot(xs,ys)
        plt.arrow(0, 0, M[i,0], M[i,1], length_includes_head=True, head_width=0.4, width=0.1, facecolor=colors[i], edgecolor=colors[i])
        plt.annotate(rf'$V_{i}$', xy=(M[i,0], M[i,1]))
        
    xmax = max(np.ceil(maxes[0]) + 1, 1)
    ymax = max(np.ceil(maxes[1]) + 1, 1)
    xmin = min(np.floor(mins[0]) - 1, -1)
    ymin = min(np.floor(mins[1]) - 1, -1)
    
    print(f'\nx-bounds: [{xmin}, {xmax}]')
    print(f'y-bounds: [{ymin}, {ymax}]')
    
    plt.plot(0,0, 'ok') # plot a black point at the origin
    plt.xlim((xmin, xmax)) # set the x axis limits
    plt.ylim((ymin, ymax)) # set the y axis limits
    #plt.legend(['V'+str(i+1) for i in range(cols)]) # give a legend
      
    plt.grid(visible=True, which='major') # plot grid lines
    plt.show()
    
def print_matrix(matrix):
    for row in matrix:
        print(row)
    
def determinant_value_inputer():
    n = int(input('\nInput the size of your matrix: '))
    
    matrix = []
    for row in range(1, n+1):
        row_list = []
        for col in range(1, n+1):
            row_list.append(int(input(f'Value at row {row}, col {col}: ')))
        matrix.append(row_list)
    
    print('\nThe determinant of the matrix\n')
    print_matrix(matrix)
    print(f'\nis {determinant_calculator(n, matrix)}')

def determinant_calculator(n, matrix):   
    if n<1:
        return None
    elif n == 1:
        return matrix[0][0]
    else:
        c_list = []
        multiplier = 1
        for a in range(0,n):
            new_matrix = []
            for row in range(0,n):
                row_list = []
                for col in range(0, n):
                    if row != 0 and col != a:
                        row_list.append(matrix[row][col])
                new_matrix.append(row_list)
            new_matrix.pop(0)
            c = multiplier * matrix[0][a] * determinant_calculator(n-1, new_matrix)
            c_list.append(c)
            multiplier *= -1
        return sum(c_list)

def scalar_matrix_multiplication(c, m):
    res = []
    
    for row in m:
        lst = []
        for val in row:
            newval = c * val
            lst.append(newval)
        res.append(lst)
    
    return res

def matrix_matrix_multiplication(m1, m2):
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])
    
    if c1 != r2:
        return None
    
    res = []
    for i in range(r1):
        lst = []
        for j in range(c2):
            lst.append(0)
        res.append(lst)
    
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j] += m1[i][k] * m2[k][j]
    
    return res

def matrix_multiplication_from_console():
    aSize = input('\nInput the size of matrix A ("{rows} {cols}"): ')
    aRow = int(aSize.split()[0])
    aCol = int(aSize.split()[1])
    A = []
    for row in range(1, aRow+1):
        row_list = []
        for col in range(1, aCol+1):
            row_list.append(float(input(f'Value at row {row}, col {col}: ')))
        A.append(row_list)
        
    bSize = input('\nInput the size of matrix B ("{rows} {cols}"): ')
    bRow = int(bSize.split()[0])
    bCol = int(bSize.split()[1])
    
    if(aCol != bRow):
        print('\nINVALID MATRIX SIZE, PLEASE TRY AGAIN')
        return None
        
    B = []
    for row in range(1, bRow+1):
        row_list = []
        for col in range(1, bCol+1):
            row_list.append(float(input(f'Value at row {row}, col {col}: ')))
        B.append(row_list)
    
    res = matrix_matrix_multiplication(A, B)
    
    print_matrix(A)
    print('\nmultiplied by\n\n')
    print_matrix(B)
    print('nis:\n\n')
    print_matrix(res())
    
def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    
    res = []
    for i in range(cols):
        lst = []
        for j in range(rows):
            lst.append(m[j][i])
        res.append(lst)
    
    return res
    

def lin_reg_normal_eq():
    aSize = input('\nInput the size of matrix A ("{rows} {cols}"): ')
    aRow = int(aSize.split()[0])
    aCol = int(aSize.split()[1])
    A = []
    for row in range(1, aRow+1):
        row_list = []
        for col in range(1, aCol+1):
            row_list.append(float(input(f'Value at row {row}, col {col}: ')))
        A.append(row_list)
        
    bRow = aRow
    bCol = 1
    B = []
    print("\nNow input the values for matrix B:  ")
    for row in range(1, bRow+1):
        row_list = []
        for col in range(1, bCol+1):
            row_list.append(float(input(f'Value at row {row}, col {col}: ')))
        B.append(row_list)
    
    ATA = matrix_matrix_multiplication(transpose_matrix(A), A)
    ATb = matrix_matrix_multiplication(transpose_matrix(A), B)
    
    print('\n\nThe matrix ATA is:')
    print_matrix(ATA)
    print('\nThe matrix ATb is:')
    print_matrix(ATb)



contin = True
print('Welcome to the Linear Algebra Operations Calculator/Visualizer.')
while(contin):
    kb = input('\n\nWhat would you like to do? (enter the letter):\n\na) graph 2d vectors\nb) calculate determinant\nc) multiply matrices\nd) calculate linear regression equations\ne) exit program\n\n')
    if kb == 'a':
        vector_grapher_2d()
    elif kb == 'b':
        determinant_value_inputer()
    elif kb == 'c':
        matrix_multiplication_from_console()
    elif kb == 'd':
        lin_reg_normal_eq()
    elif kb == 'e':
        contin = False
    else:
        print('Unknown Input, please try again.\n')

print('\nHave a great day!')

