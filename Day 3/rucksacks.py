#%%
"""
part 1: identify scores of character shared in the first and second half of a 
string
"""
total1 = 0
lst = []

# read input
with open('Input/input.txt','r') as f:
    lines = f.readlines()

# create scoring function using ord() method
def scoreCharacter (character):
    if character.isupper():
        score = ord(character) - 38 # ord method changes char to int
    elif character.islower():
        score = ord(character) - 96
    return score
    
for line in lines: 
    line = line.strip()
    n = len(line)
    str1 = line[0:n//2]
    str2 = line[n//2:]
    shared = ''.join(set(str1).intersection(str2)) # shared characters identified as set intersection
    score = scoreCharacter(shared)
    lst.append(line)
    total1 += score
        
print(f'Priority sum of shared compartments is:  {total1}')

#%%
"""
part 2: identify scores of character shared by groups of 3 strings
"""
total2 = 0

import numpy as np  
groups = np.array_split(lst,len(lst)/3)

for group in groups:
    elf1 = group[0]
    elf2 = group[1]
    elf3 = group[2]
    shared = ''.join(set(elf1).intersection(elf2).intersection(elf3))
    score = scoreCharacter(shared)
    total2 += score
    
print(f'Priority sum of badges is:  {total2}')