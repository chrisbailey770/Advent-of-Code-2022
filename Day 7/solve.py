# -*- coding: utf-8 -*-
"""
Created on Wed Dec 7 08:53:57 2022

@author: chris
"""

import os
from re import search

os.chdir('C:/Users/chris/Dropbox/Programming Practice/Advent of Code 2022/Day 7')

with open('Input/input.txt') as f:
    rows = f.readlines()

# rows = []
# for line in lines:
#     line = line.strip('\n')
#     rows.append(line)

# '$ cd /' = change directory to outer most
# '$ cd abc' = change directory to abc
# '$ cd x' = find child directory x and change to it
# '$ cd ..' = find parent directory and change to it
# '$ ls' = list directories and files in current directory
# '123 abc' = directory has file abc with size 123
# 'dir xyz' = current directory contains directory xyz

# try reproducing example
root = os.getcwd()
child_dir = os.path.join(root, 'part1')
os.chdir(child_dir)
root = os.getcwd()

# create directories of files where value is the filename
for row in rows[0:26]:
    row = row.strip('\n')
    current_dir = os.getcwd()
    if search('cd', row):
        if search('cd /', row):
            os.chdir(root)
        elif search('cd ..', row):
            os.chdir('..')
        else:
            child_dir = os.path.join(current_dir, row[5:])
            os.chdir(child_dir)
    elif search('ls', row[2:4]):
        os.listdir()
    elif search('dir', row):
        child_dir = os.path.join(current_dir, row[4:])
        if not os.path.exists(child_dir):
               os.makedirs(child_dir)
    else:
        open(row.split()[0], 'w').close()
        
# get list of directories
dir_list = [x[0] for x in os.walk(root)]
file_ints = []
sums_under_100000 = []
for d in dir_list:
    print(d)
    for (dirpath, dirnames, filenames) in os.walk(d):
        file_ints += [int(file) for file in filenames]
    file_sum = sum(file_ints)
    print(file_sum)
    if file_sum <= 100000:
        sums_under_100000.append(file_sum)
    file_ints = []

print(sum(sums_under_100000))    
  
            
        