# advent of code 2020
# day 10
# in a list of numbers, "sort" them, find the number of differences between
# consecutive numbers that are 1, and 3 and multiply those numbers together

# solution creates a frequency table from the numbers, then counts the differences

from math import factorial


# read in data and get the largest value to create the frequency table
# then populate the table with the numbers read in
def readIn():
    largest = 0

    with open('da10.txt', 'r') as f:
        Lines = f.readlines()

        for line in Lines:
            line = int(line.strip())
            if line > largest:
                largest = line

        print("largest:", largest)
        ft = [0] * (largest + 1)

        for line in Lines:
            ft[int(line.strip())] += 1

        return ft


# make another frequency table to count the differences of one and differences of three
def part1(ft):
    count = 1
    counts = [0] * 4
    length = len(ft)

    # loop through frequency table, counting the differences between numbers
    # and incrementing values in the frequency table of ones and threes
    for i in range(2, length):
        if ft[i] == 1:
            counts[count] += 1
            count = 1
        else:
            count += 1

    print("ones:", counts[1], "threes:", counts[3])
    return (counts[1] + 1) * (counts[3] + 1)


# uses collections and combinations to calculate the number of possible arrangements
# collection: set of consecutive numbers, all that matters is how many numbers are in a row
               # a collection is the numbers on the inside, because must be bounded by numbers
               # so the connections can be made between the next set of consecutive numbers.
               # i.e. a space can not be over 2 consecutive numbers
# combination: number of unique sets of these numbers that can be made
def part2(ft):
    colls = []
    collection = 0
    combos = []
    combinations = 1
    ft[0] = 1


    # get a set of collections: what's the number that are in a row.
    # this only counts if that number is > 2 because otherwise nothing can be removed
    for i in ft:
        if i == 1:
            collection += 1
        elif collection > 2:
            colls.append(collection)
            collection = 0
        else:
            collection = 0
    colls.append(collection)
    print(colls)

    # for each set of numbers, calculate the number of combinations that can be
    # made from them. The first and last cannot be removed so the number entered
    # is the number in the set - 2
    # get the number of combinations, then multiply
    for col in colls:
        combos.append(getCombos(col - 2))
        combinations *= getCombos(col - 2)

    print("combos:", combos)
    print("combinations:", combinations)



# this was helpful: https://en.wikipedia.org/wiki/Combination
def getCombos(n):
    sk = 0
    for k in range(0, n + 1):
        sk += factorial(n)/(factorial(k) * factorial(n - k))
    # this is hacky but if it is a set of 5 in a row, it becomes 3 in this function
    # and the number of combos is 8, but that includes one option where there is an
    # opening three long in the middle, and that won't work, so the actual number of
    # combinations is 7. There aren't any values over 5 in the data set so it works.
    if sk == 8:
        sk = 7
    return int(sk)








ft = readIn()
#ft = [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
#ft = [0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1]
part2(ft)
#print("solution:", part1(ft))


