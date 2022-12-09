# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:49:07 2022

@author: chris
"""

import numpy as np

# define rope task
def rope_task(instructions, knots):
    
    # dictionaries for directional counting
    updown = {'U': 1, 'D': -1}
    rightleft = {'R': 1, 'L': -1}
    
    # iniitalize list where each pair is the position of a knot
    ropesegs = [[0, 0] for _ in range(knots)]
    
    # store uniques visited in a set
    visited = set()
    
    # get each instruction
    for instruction in instructions:
        direction, steps = instruction.split()
        
        # apply steps according to dictionary
        for i in range(0, int(steps)):
            ropesegs[0][0] += updown.get(direction, 0)
            ropesegs[0][1] += rightleft.get(direction, 0)
            
            # find head-tail distance in the x and y directions
            for i in range(0, len(ropesegs)-1):
                updown_dist = ropesegs[i][0]-ropesegs[i+1][0]
                leftright_dist = ropesegs[i][1]-ropesegs[i+1][1]
                
                # change tail state if distance exceeds rope length
                if updown_dist**2 + leftright_dist**2 > 2: 
                    ropesegs[i+1][0] += np.sign(updown_dist)
                    ropesegs[i+1][1] += np.sign(leftright_dist)
                    
            # add tail state set        
            visited.add(str(ropesegs[-1]))
    
    # return number of different tail states visited
    return visited

# parse data
with open('Input/input.txt') as f: 
    lines = [line.strip('\n') for line in f.readlines()]

# part 1 - two knots in rope 
visited = rope_task(lines, 2)
print(f'part 1 visited tail states: {len(visited)}')

# part 2 - 10 knots in rope
visited2 = rope_task(lines, 10)
print(f'part 2 visited tail states: {len(visited2)}')

