# -*- coding: utf-8 -*-
"""
part 1: identify pairs with overlapping number lists
part 2:
"""

with open('Input/input.txt','r') as f:
    lines = f.readlines()

# strip spaces and escape characters, pairs in nested list
lines = [line.strip() for line in lines if line != '']   
pairs = [line.split(',') for line in lines]

# create arrays of number ranges, 
# use all() to check if all elements exist in the comparison list
# use any() to check if any element exists in the comparison list
count1 = 0
count2 = 0
for pair in pairs:    
    item1 = pair[0].split('-')
    item1 = [int(x) for x in item1]
    item2 = pair[1].split('-')
    item2 = [int(x) for x in item2]
    array1 = [x for x in range(item1[0], item1[1]+1)]
    array2 = [x for x in range(item2[0], item2[1]+1)]
    if all(x in array1 for x in array2) or all(x in array2 for x in array1):
        count1 += 1
    if any(x in array1 for x in array2) or any(x in array2 for x in array1):
        count2 += 1

print(f'Total number of pairs where one range contains the other: {count1}')
print(f'Total number of pairs where one range has elements of the other: {count2}')
