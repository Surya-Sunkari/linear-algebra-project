# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:13:04 2022

@author: 100031985
"""

import numpy as np
import matplotlib.pyplot as plt

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
    
    print(M, 'M')
    
    rows,cols = M.T.shape
    
    # get absolute maxes for axis ranges to center origin, adds buffer space
    maxes = 1.1*np.amax(M, axis = 0)
    mins = 1.1*np.amin(M, axis=0)
    
    print(maxes, 'maxes')
    print(mins, 'mins')
    
    for i,l in enumerate(range(0,cols)):
        xs = [0,M[i,0]]
        ys = [0,M[i,1]]
        plt.plot(xs,ys)
    
    xmax = np.ceil(maxes[0]) + 1
    ymax = np.ceil(maxes[1]) + 1
    xmin = np.floor(mins[0]) - 1
    ymin = np.floor(mins[1]) - 1
    
    print(xmin, xmax, 'xbounds')
    print(ymin, ymax, 'ybounds')
    
    plt.plot(0,0, 'ok') # plot a black point at the origin
    plt.axis('equal')  # set the axes to the same scale
    plt.xlim((xmin, xmax)) # set the x axis limits !!! problem setting limits for x and y axis
    plt.ylim((ymin, ymax)) # set the y axis limits
    plt.legend(['V'+str(i+1) for i in range(cols)]) # give a legend
    plt.grid(visible=True, which='major') # plot grid lines
    plt.show()
    
vector_grapher_2d()
