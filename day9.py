# advent of code 2020
# day 9
# which number isn't the sum of two of the previous 25 numbers

from queue import Queue

def readIn():
    count = 0
    numbers = []

    with open('da9.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            numbers.append(int(line.strip()))
            count += 1
        print(count)
    if f.closed:
        return numbers
    else:
        print("error closing file")
        return []


def part1(numbers):
    adds = Queue(25)

    for num in numbers:
        if adds.full() is False:
            adds.put(num)
        else:
            if checksums(adds, num) is False:
                return num
            if adds.empty() is True:
                print("empty queue")
            else:
                adds.get()
                adds.put(num)
    return -1

def checksums(adds, number):
    size = 25
    items = []

    for j in range(0,25):
        items.append(adds.get())
        adds.put(items[j])

    for i in range(0, size - 1):
        for c in range(i + 1, size):
            if items[i] + items[c] == number:
                return True

    return False

def part2(numbers, found):
    i = j = 0
    first  = last = numbers[i]
    total = 0

    while total != found:
        if total < found or j == i:
            i += 1
            last = numbers[i]
            total += last
        else:
            total -= first
            j += 1
            first = numbers[j]

    return first + last






#def part2(numbers, found):
#    adds = Queue()
#    return findCons(numbers, adds, found, 0)

#def findCons(numbers, adds, found, index):
#    total = 0
#    if index == len(numbers):
#        return -1
#    length = adds.qsize()
#    for i in range(0, length):
#        if adds.empty() is False:
#            value = adds.get()
#            adds.put(value)
#            total += value
#    if total == found:
#        return adds.get() + getLast(adds)
#    if total < found:
#        adds.put(numbers[index])
#        return findCons(numbers, adds, found, index + 1)
#    if adds.empty() is True:
##        return findCons(numbers, adds, found, index + 1)
#    adds.get()
#    return findCons(numbers, adds, found, index)


#def getLast(adds):
#    while adds.empty() is False:
#        last = adds.get()
#    return last



numbers = readIn()
found = part1(numbers)
print(part2(numbers, found))
