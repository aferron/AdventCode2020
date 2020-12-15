# advent of code
# Day 1
# find two numbers that add up to 2020 and multiply them together
countIn = 0
countFound = 0
puzzleInput = []
found = [0] * 2021
diff2 = 0
diff0 = 0
diff1 = 0
done = 0

with open('day1PuzzleInput.txt', 'r') as f:
    Lines = f.readlines()
    for line in Lines:
        puzzleInput.append(int(line.strip()))
        countIn += 1
print(countIn)


if f.closed:
    for x in puzzleInput:
        found[x] = 1
        countFound += 1

    for j in range (0, 200):
        val1 = puzzleInput[j]
        diff1 = 2020 - val1
        k = j + 1
        for k in range (k, 200):
            val2 = puzzleInput[k]
            if val2 < diff1:
                val3 = diff1 - val2
                if found[val3]:
                    print(val1, " + ", val2, " + ", val3, " = ", val1 + val2 + val3)
                    done = 1
            if(done == 1):
                break
        if(done == 1):
            break


    if(found[val1]):
        print("found ", val1)
    else:
        print("not found ", val1)
    if(found[val2]):
        print("found ", val2)
    else:
        print("not found ", val2)
    if(found[val3]):
        print("found ", val3)
    else:
        print("not found ", val3)

print(val1, " * ", val2, " * ", val3, " = ", val1 * val2 * val3)
