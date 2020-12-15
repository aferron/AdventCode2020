# advent of code 2020
# day 6
# count the number of unique questions per group, then add those together for the plane


from enum import Enum


def readin():
    groups = []
    group = ""
    count = 0
    people = 0

    with open('da6.txt', 'r') as f:
        Lines = f.readlines()
        # read in all the lines, then go through them
        # this takes data from multiple lines and combines to a single line
        for line in Lines:
            # newline separates each group
            if line != "\n":
                group += line.strip()
                people += 1
            else:
                # add to the list of groups
                groups.append([group, people])
                group = ""
                people = 0
            count += 1
        # one more append to catch the last entry not appended in loop above
        groups.append([group, people])

    if f.closed:
        return groups
    else:
        print("error closing file")


def count_uniques(group):
    count = 0
    length = len(group[0])
    tally = [0] * 26

    letters = list(group[0])

    for l in letters:
        index = ord(l) - 97
        tally[index] += 1

    for i in range(0,26):
        if tally[i] == group[1]:
            count += 1

    return count

def part1(groups):
    count = 0

    for group in groups:
        count += count_uniques(group)
    return count

print(part1(readin()))






