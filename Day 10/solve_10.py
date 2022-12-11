# -*- coding: utf-8 -*-

import numpy as np

with open('Input/input.txt') as f:
    lines = [line.strip('\n') for line in f]

cycle = 0 # increase by 2 if addx, by 1 if noop
register = 1 # increase by value of addx
row = 0
col = 0
pixel = 0 
sprite = [register-1, register, register+1] # horz position of sprite

strength_checks = [20, 60, 100, 140, 180, 220, 260]
image_checks = [40, 80, 120, 160, 200, 240]
signal_strength = []

image = np.chararray((6,40))
image[:] = '.'

def update_image(register, cycle, image, row):
    pos = (cycle-1) % 40
    if pos in {register-1, register, register+1}:
        image[row,pos] = '#'
    return image

for line in lines:
    cycle += 1 # cycle once
    if cycle in image_checks:
        row += 1
    image = update_image(register, cycle, image, row)
    if cycle in strength_checks:
        signal_strength.append(cycle*register)
    if line.find('addx') > -1: # addx command requires second cycle, addition, and second check
        _, val = line.split()
        cycle += 1 # cycle again with add command
        if cycle in image_checks:
            row += 1
        image = update_image(register, cycle, image, row)
        if cycle in strength_checks:
            signal_strength.append(cycle*register)
        register += int(val)
        sprite = [register-1, register, register+1]

print(f'part 1 summed signal strength: {sum(signal_strength)}')
print(f'part 2 rendered letters: \n {image}')
