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



class solution:
    def __init__(self, part1path=[]):
        self.part1path = part1path

    def readIn(self):
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

    def part1(self, instructions):
        accumulator = 0
        index = 0
        ins = instructions[index]

        while ins.visited is False:
            ins.visited = True
            self.part1path.append(ins)
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

    def reachEnd(self, instructions, ind, acc):
        accumulator = acc
        index = ind
        ins = instructions[index]
        length = len(instructions)
        visits = [False] * length

        while visits[index] is False:
            visits[index] = True
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
            if index == length:
                print("final value when end reached is: ", accumulator)
                return True
            ins = instructions[index]

        return False


    def startAndSwitch(self, instructions):
        accumulator = 0
        index = 0
        ins = instructions[index]
        length = len(instructions)
        visits = [False] * length

        while visits[index] is False:
            visits[index] = True
            if ins.function == 'acc':
                accumulator += ins.value
                index += 1
            elif ins.function == 'jmp':
                if self.reachEnd(instructions, index + 1, accumulator) is True:
                    return True
                index += ins.value
            elif ins.function == 'nop':
                if self.reachEnd(instructions, index + ins.value, accumulator) is True:
                    return True
                index += 1
            else:
                print('error')
                break
            ins = instructions[index]

        return False 



solved = solution()
read = solved.readIn()
print(solved.startAndSwitch(read))
