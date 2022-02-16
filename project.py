# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:13:04 2022

@author: 100031985
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

#https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#sphx-glr-gallery-text-labels-and-annotations-text-fontdict-py
#text stuff

"""
Plan:
    simple 2d vector grapher
    determinant calculator for 2d and 3d matrices (should plot determinant for 2d matrices)
    transformation calculator and viewer for 2d matrices
    matrix multiplication calculator ? (could be standalone)
"""

def get_vectors_2d():
    vectors = []
    
    while True:
        kb = input('enter a 2d vector separated by a space, or "done" when finished:  ')
        if kb == 'done':
            break
        kb = kb.split()
        try:
            vectors.append([int(kb[0]), int(kb[1])])
        except:
            print('problem with your input. make sure to follow "x y" format')
        else:
            print('vector appended')
    
    return vectors

def vector_grapher_2d():
    M = np.array(get_vectors_2d())
    colors = list(mcolors.BASE_COLORS)
    print(len(colors))
    
    print(M, 'M')
    
    rows,cols = M.T.shape
    
    # get absolute maxes for axis ranges to center origin, adds buffer space
    maxes = 1.1*np.amax(M, axis = 0)
    mins = 1.1*np.amin(M, axis=0)
    
    print(maxes, 'maxes')
    print(mins, 'mins')
    
    for i,l in enumerate(range(0,cols)):
        #xs = [0,M[i,0]]
        #ys = [0,M[i,1]]
        #plt.plot(xs,ys)
        plt.arrow(0, 0, M[i,0], M[i,1], length_includes_head=True, head_width=0.4, width=0.1, facecolor=colors[i], edgecolor=colors[i])
    
    xmax = max(np.ceil(maxes[0]) + 1, 1)
    ymax = max(np.ceil(maxes[1]) + 1, 1)
    xmin = min(np.floor(mins[0]) - 1, -1)
    ymin = min(np.floor(mins[1]) - 1, -1)
    
    print(xmin, xmax, 'xbounds')
    print(ymin, ymax, 'ybounds')
    
    plt.plot(0,0, 'ok') # plot a black point at the origin
    plt.xlim((xmin, xmax)) # set the x axis limits
    plt.ylim((ymin, ymax)) # set the y axis limits
    plt.legend(['V'+str(i+1) for i in range(cols)]) # give a legend
    plt.grid(visible=True, which='major') # plot grid lines
    plt.show()

    
def print_matrix(matrix):
    for row in matrix:
        print(row)
    
def determinant_value_inputer():
    n = int(input('input the size of your matrix: '))
    
    matrix = []
    for row in range(1, n+1):
        row_list = []
        for col in range(1, n+1):
            row_list.append(int(input(f'value at row {row}, col {col}: ')))
        matrix.append(row_list)
    
    print('\nthe determinant of the matrix\n')
    print_matrix(matrix)
    print(f'\nis {determinant_calculator(n, matrix)}')

def determinant_calculator(n, matrix):   
    if n<1:
        return None
    elif n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
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
            print(new_matrix)
            c = multiplier * a * determinant_calculator(n-1, new_matrix)
            c_list.append(c)
            multiplier *= -1
        return sum(c_list)
    
#vector_grapher_2d()
determinant_value_inputer()
#print_matrix([[1,2,3],[4,25,6],[17,8,9]])
