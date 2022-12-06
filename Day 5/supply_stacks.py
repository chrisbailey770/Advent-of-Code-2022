with open('Input/input.txt','r') as f:
    data = f.readlines()
  
n_stacks = int(len(data[0])/4) # n_stacks = 9
stacks = [[] for i in range(n_stacks)] # nested list representing stacks
final = []

# parse input
for row in data[:8]: 
    for stack in range(n_stacks):
        index = 4 * stack + 1
        if row[index] == ' ':
            continue
        stacks[stack].append(row[index])

#%% part 1: moving one box at a time - top box becomes bottom box
class stack1:
    crates = []
    def __init__(self):
        self.crates = stacks
    def move(self, amount, starting_stack, ending_stack):
        movers = self.crates[starting_stack-1][:amount][::-1]
        self.crates[starting_stack-1] = self.crates[starting_stack-1][amount:]
        self.crates[ending_stack-1] = movers + self.crates[ending_stack-1]
    def print_top_crates(self):
        for stack in self.crates:
            print(stack[0], end='')
            
# initialize object for stack class and call move method per line
cargo1 = stack1()
for row in data[10:]:
    str_parts = row.strip('\n').split(' ')
    cargo1.move(int(str_parts[1]), 
               int(str_parts[3]),
               int(str_parts[5]))
    
cargo1.print_top_crates()
        
#%% part 2: moving all boxes - order maintained

class stack2:
    crates = []
    def __init__(self):
        self.crates = stacks
    def move(self, amount, starting_stack, ending_stack):
        movers = self.crates[starting_stack-1][:amount]
        self.crates[starting_stack-1] = self.crates[starting_stack-1][amount:]
        self.crates[ending_stack-1] = movers + self.crates[ending_stack-1]
    def print_top_crates(self):
        for stack in self.crates:
            print(stack[0], end='')
            
# initialize object for stack class and call move method per line
cargo2 = stack2()
for row in data[10:]:
    str_parts = row.strip('\n').split(' ')
    cargo2.move(int(str_parts[1]), 
               int(str_parts[3]),
               int(str_parts[5]))
    
cargo2.print_top_crates()