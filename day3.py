# advent of code
# day 3
# how many trees does the toboggan encounter
# part 1: on a slope of 3 right, 1 down

def readin():
    landscape = []
    countIn = 0

    with open('da3.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            landscape.append(line.strip())
            countIn += 1
    return landscape

def part1(n, m, terr):
    count = 0
    index = 0
    width = len(terr[0])
    length = len(terr)

    for i in range(0, length):
        if i % m == 0:
            if terr[i][index] == '#':
                count += 1
            index = (index + n) % width
    return count





terrain = readin()
a = part1(1,1,terrain)
b = part1(3,1,terrain)
c = part1(5,1,terrain)
d = part1(7,1,terrain)
e = part1(1,2,terrain)
print(a,",",b,",",c,',',d,',',e)
print(a*b*c*d*e)

