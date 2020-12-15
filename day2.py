# advent of code
# day 2
# how many entries are invalid

class password:
    def __init__(self, a, b, c, d):
        self.low = a
        self.high = b
        self.letter = c
        self.string = d


def part1(inps):
    count = 0
    valid = 0
    for entry in inps:
        for char in entry.string:
            if(char == entry.letter):
                count += 1
        if count >= entry.low and count <= entry.high:
            valid += 1
        count = 0
    return valid

def part2(inps):
    valid = 0
    for entry in inps:
        a = entry.string[entry.low - 1] == entry.letter
        if entry.high - 1 < len(entry.string):
            b = entry.string[entry.high - 1] == entry.letter
            if (a or b) and not(a and b):
                valid += 1
        #print(entry.letter, ",", entry.string[entry.low - 1], ",", end='')
        #if entry.high < len(entry.string):
            #print(entry.string[entry.high - 1])
        #else:
            #print("out of range")
    return valid



def readin():
    countIn = 0
    inps = []
    passwords = []

    with open('da2.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            inp = line.strip().split(' ')
            inp[0] = inp[0].split('-')
            inp[1] = inp[1].rstrip(':')
            pwd = password(int(inp[0][0]), int(inp[0][1]), inp[1], inp[2])
            inps.append(pwd)
            countIn += 1
    return inps

passwordList = readin()
print(part1(passwordList))
print(part2(passwordList))




