# advent of code 2020
# day 8
# follow instructions to find the infinite loop


class instruct:
    def __init__(self, function='', value=0, visited=False):
        self.function = function
        self.value = value
        self.visited = visited

    def display(self):
        print(self.function, " ", self.value, " V: ", self.visited)

def readIn():
    count = 0
    readLines = []
    instructions = []

    with open('da8.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            readline = line.replace('\\', '').strip()
            ins = readline.split(' ')
            instruction = instruct(ins[0], int(ins[1]))
            instructions.append(instruction)
            count += 1
    return instructions

def part1(instructions):
    accumulator = 0
    index = 0
    ins = instructions[index]

    while ins.visited is False:
        ins.visited = True
        if ins.function == 'acc':
            accumulator += ins.value
            index += 1
        elif ins.function == 'jmp':
            index += ins.value
        elif ins.function == 'nop':
            index += 1
        else:
            print('error')
            break
        ins = instructions[index]

    return accumulator

def part2(instructions):
    accumulator = 0
    index = 0
    ins = instructions[index]
    length = len(instructions)
    c = 0
    changed = False

    for i in range(0,length):
        while ins.visited is False:
            if ins.function == 'acc':
                accumulator += ins.value
                index += 1
            elif ins.function == 'jmp':
                if c == i and changed is False:
                    ins.function = 'nop'
                    changed = True
                    print("changed at c =", c)
                else:
                    index += ins.value
            elif ins.function == 'nop':
                if c == i and changed is False:
                    ins.function = 'jmp'
                    changed = True
                    print("changed at c =", c)
                else:
                    index += 1
            else:
                print('error')
                break
            if index == length:
                break
            ins = instructions[index]
        c += 1
        changed = False
        if index == length:
            break

    return accumulator

read = readIn()
print(part2(read))
        
