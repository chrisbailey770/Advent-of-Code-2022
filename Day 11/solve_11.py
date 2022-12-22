import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def monkey_data(seq, size):
    data = [seq[pos:pos + size] for pos in range(0, len(seq), size)]
    return data


def data_to_dict(item):
    output = dict()
    output['id'] = item[0][-2]
    items = item[1].split(':')[1].split(',')
    items = [int(x.replace(' ', '')) for x in items]
    output['items'] = items
    output['operation'] = ops[item[2].split(':')[1].split(' ')[-2]]
    if item[2].endswith('old'):
        output['number'] = 'square'
    else:
        output['number'] = int(item[2].split(':')[1].split(' ')[-1])
    output['divisor'] = int(item[3].split(':')[1].split(' ')[-1])
    output['true_monkey'] = int(item[4][-1])
    output['false_monkey'] = int(item[5][-1])
    return output


class Monkey():
    
    def __init__(self, dict):
        self.id = dict['id']
        self.items = dict['items']
        self.operation = dict['operation']
        self.number = dict['number']
        self.divisor = dict['divisor']
        self.true_monkey = dict['true_monkey']
        self.false_monkey = dict['false_monkey']
        self.processed_items = 0
        
        
    def receive_item(self, item):
        self.items.append(item)
        
        
    def monkey_partners(self, all_monkeys):
        self.true_monkey = all_monkeys[self.true_monkey]
        self.false_monkey = all_monkeys[self.false_monkey]

    
    def process_items(self, part):
        # apply operation to first item in queue: this is worry
        for item in self.items:
            if self.number == 'square':
                item = self.operation(item, item)
            else:
                item = self.operation(item, self.number)
            # Part 1: bored, floor divide worry by 3
            if part == 1:
                item = item // 3
            else:
                item = item % monkeymod
            # divisible check: if true, pass worry to true partner. else pass worry to false partner
            if item % self.divisor == 0:
                self.true_monkey.receive_item(item)
            else:
                self.false_monkey.receive_item(item)       
            self.processed_items += 1
        self.items = []
        
        
with open('Input/input.txt', 'r') as f:
    lines = f.read().splitlines()

monkeys = []
monkeymod = 1

data = monkey_data(lines, 7)

for item in data:
    dic = data_to_dict(item)
    monkeys.append(Monkey(dic))
    monkeymod *= int(dic["divisor"])
    
for m in monkeys:
    m.monkey_partners(monkeys)

# n_rounds_1 = 20
# for i in range(n_rounds_1):
#     for m in monkeys:
#         m.process_items(part=1)
        
# monkey_stuff = sorted([x.processed_items for x in monkeys], reverse=True)

# print('monkey business part 1 = ', monkey_stuff[0] * monkey_stuff[1])    

n_rounds_2 = 10000
for i in range(n_rounds_2):
    if i % 10 == 0:
        print(i)
    for m in monkeys:
        m.process_items(part=2)
        
monkey_stuff = sorted([x.processed_items for x in monkeys], reverse=True)

print('monkey business part 2 = ', monkey_stuff[0] * monkey_stuff[1])    

