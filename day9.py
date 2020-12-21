# advent of code 2020
# day 9
# part 1: which number isn't the sum of two of the previous 25 numbers
# part 2: find a set of numbers that add to the number found in part 1,
#         then sum the smallest and largest numbers within that set

from queue import Queue

# reading in, only need to strip the newline off the ned and input into a list
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


# use a queue to keep the last 25 numbers
def part1(numbers):
    adds = Queue(25)

    for num in numbers:
        # first fill the queue with 25 numbers
        if adds.full() is False:
            adds.put(num)
        # then check if two of the numbers in the queue add up to the following number
        # if not, remove the last entered and add the next number in the list
        else:
            if checksums(adds, num) is False:
                return num
            if adds.empty() is True:
                print("empty queue")
            else:
                adds.get()
                adds.put(num)
    return -1


# check if two of the numbers in the queue add up to the target number
def checksums(adds, number):
    size = 25
    items = []

    # make a list from the queue
    for j in range(0,25):
        items.append(adds.get())
        adds.put(items[j])

    # traverse the list checking if any two add up to the target number
    for i in range(0, size - 1):
        for c in range(i + 1, size):
            if items[i] + items[c] == number:
                return True

    return False


# traverse the list to find a set of consecutive numbers that add up to the
# target number
def part2(numbers, found):
    i = j = 0
    first  = last = numbers[i]
    total = numbers[i]
    length = len(numbers)
    print("found:", found)


    # loop as long as we haven't found a set that sums to the target number
    # and we're not at the end of the list
    while total != found and i < length - 1:
        # if our set sums to a smaller number than the target,
        # add to the set by incrementing the leading index
        if total < found or j == i:
            i += 1
            last = numbers[i]
            total += last
        # if our set sums to a larger number than the target,
        # add to the set by incrementing the trailing index
        else:
            total -= first
            j += 1
            first = numbers[j]
        #print("first:", first, "last:", last, "total:", total)

    #print("i:", i, "j:", j)

    # loop to find the smallest and largest numbers in the set
    smallest = largest = numbers[j]
    for k in range(j + 1, i + 1):
        if(numbers[k] < smallest):
            smallest = numbers[k]
        elif(numbers[k] > largest):
            largest = numbers[k]
    print("largest:", largest, "smallest:", smallest)

    return largest + smallest




numbers = readIn()
#numbers = [35,20,15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
found = part1(numbers)
print("found:", found)
print(part2(numbers, found))
