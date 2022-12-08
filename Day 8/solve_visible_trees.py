with open('Input/input.txt','r') as f:
    lines = f.readlines()

import numpy as np

lst = []
for i, line in enumerate(lines):
    line = [int(x) for x in line.strip('\n')]
    lst.append(line)

# create matrix of trees    
D = np.array(lst)
n_rows, n_cols = D.shape

# create a bool for each element representing whether the integer exceeds those
# - above it      D[:row,col]
# - below it      D[row+1:,col]
# - left of it    D[row,:col]
# - right of it   D[row,col+1:]
# ignore elements in borders (D[0,:], D[-1,:], D[:,0], D[:,-1])

Vis = np.zeros(shape=D.shape)
for row in range(n_rows):
    
    for col in range(n_cols):
        val = D[row,col]
        
        if row == 0 or row == n_rows-1 or col == 0 or col == n_cols-1:
            pass   
        
        else:
            if (
                    np.all(val > D[:row,col]) or
                    np.all(val > D[row+1:,col]) or
                    np.all(val > D[row,:col]) or 
                    np.all(val > D[row,col+1:])
               ):
                Vis[row,col] = 1

# count visible trees
n_border = n_rows*2 + (n_cols-2)*2
n_visible = int(np.sum(Vis))
print(f'total visible trees: {n_border  + n_visible}')

#%% part 2: trees visible from inside

# function to count visible trees in given array
def count_visible(array, tree):
    count = 1
    for i in range(len(array)):
        if tree > array[i] and i < len(array)-1:
            count += 1
        else:
            break
    return count

Vis_from_inside = np.zeros(shape=D.shape)
for i in range(1,n_rows-1):
    
    for j in range(1,n_cols-1):
        row = D[i,:]
        col = D[:,j]
        val = D[i,j]
        above = count_visible(col[i-1::-1],val)
        below = count_visible(col[i+1:],val)
        left =  count_visible(row[j-1::-1],val)
        right = count_visible(row[j+1:],val)
        score = above * below * right * left
        Vis_from_inside[i,j] = score
        
# identify score of best tree
print(f'highest score: {int(Vis_from_inside.max())}')