with open('Input/input.txt','r') as f:
    data = f.readlines()

#%% part 1: move windowed characters to a set to check if all unique
# start of packet if 4 consecutive characters are unique

string = data[0]
# characters = [*string]
# count = window

def find_unique_window(string, window):
    characters = [*string] # unpack string into list of characters
    count = window
    while len(set(characters[:window])) != window:
        characters.pop(0)
        count += 1
    return count

count1 = find_unique_window(string, 4)
print(count1)

#%% part 2: same method, start of message if 14 consecutive characters are unique
count2 = find_unique_window(string, 14)
print(count2)
