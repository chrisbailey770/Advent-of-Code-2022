# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:49:07 2022

@author: chris
"""

import numpy as np
    
# initial state
state = np.array([['.','.','.','.','.','.'],
           ['.','.','.','.','.','.'],
           ['.','.','.','.','.','.'],
           ['.','.','.','.','.','.'],
           ['H','.','.','.','.','.']])

n_rows, n_cols = state.shape

# define H-T distance function
def euclidean_distance(array1, array2):
    distance = np.linalg.norm(array1 - array2)
    return distance

# define state update function
def make_move(state, direction):
     (old_head_row, old_head_col) = np.where(state == 'H')
     old_head_row, old_head_col = old_head_row[0], old_head_col[0]
     old_tail_row, old_tail_col = np.where(state == 'T')
     if old_tail_row.any(): # if tail exists, temporarily make #
         old_tail_row, old_tail_col = old_tail_row[0], old_tail_col[0]
     else: # tail does not exist, it is under the head
         old_tail_row, old_tail_col = old_head_row, old_head_col
     
     if direction == 'U':
         if old_head_row == 0: # old head at row 0 cannot go up further
             pass    
         else:
             state[old_head_row,old_head_col] = '.' # old head position
             if euclidean_distance(np.array((old_head_row-1,old_head_col)),
                                   np.array((old_tail_row,old_tail_col))) >= 2:
                 state[old_head_row,old_head_col] = 'T' # tail at previous head
                 state[old_tail_row, old_tail_col] = '#' # mark previous tail position
             else:
                 state[old_tail_row,old_tail_col] = 'T'
             state[old_head_row-1,old_head_col] = 'H' # updated head position (do last for cases where head and tail indices are the same)
             
     elif direction == 'D':
         if old_head_row == 4: # old head at row 4 cannot go down further
             pass
         else:
             state[old_head_row,old_head_col] = '.'
             if euclidean_distance(np.array((old_head_row+1,old_head_col)),
                                   np.array((old_tail_row,old_tail_col))) >= 2:
                 state[old_head_row,old_head_col] = 'T'
                 state[old_tail_row, old_tail_col] = '#'
             else:
                 state[old_tail_row,old_tail_col] = 'T'
             state[old_head_row+1,old_head_col] = 'H' 
             
     elif direction == 'L':
         if old_head_col == 0: # old head at col 4 cannot go left further
             pass
         else:
             state[old_head_row,old_head_col] = '.'
             if euclidean_distance(np.array((old_head_row,old_head_col-1)),
                                   np.array((old_tail_row,old_tail_col))) >= 2:
                 state[old_head_row,old_head_col] = 'T'
                 state[old_tail_row, old_tail_col] = '#'
             else:
                 state[old_tail_row,old_tail_col] = 'T'
             state[old_head_row,old_head_col-1] = 'H'   
            
     elif direction == 'R':
         if old_head_col == 4: # old head at row 4 cannot go right further
             pass
         else:
             state[old_head_row,old_head_col] = '.'
             if euclidean_distance(np.array((old_head_row,old_head_col+1)),
                                   np.array((old_tail_row,old_tail_col))) >= 2:
                 state[old_head_row,old_head_col] = 'T'
                 state[old_tail_row, old_tail_col] = '#'
             else:
                 state[old_tail_row,old_tail_col] = 'T'
             state[old_head_row,old_head_col+1] = 'H'    
     
     return state

# parse data
with open('Input/input.txt') as f:
    lines = [line.strip() for line in f]

# update state according to instructions
for line in lines:
    print(line)
    direction, amount = line.split(' ')
    for i in range(0,int(amount)):
        state = make_move(state,direction)