import numpy as np

path = 'C:/Users/chris/Dropbox/Programming Practice/Advent of Code 2022/Day 1/'

# input as list
with open(path+'Input/input.txt') as f:
    lines = f.readlines()

# create nested list where sublists exist for each elf
# strip '\n'
counter = 0
L = [[]]
for line in lines:
    if line != '\n':
        line = line.strip()
        L[counter].append(line)
    else:
        counter += 1 
        L.append([])
        
# find top 3 elves with most total calories         
total_calories = []
for lst in L:
    int_list = [eval(i) for i in lst]
    int_array = np.array(int_list)
    total_calories.append(int_array.sum())

total_calories.sort()    
print(total_calories[-3:])
