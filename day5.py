# advent of code 2020
# day 5
# seat numbers, binary
# what is the largest seat ID (ID = row * 8 + column)
# B = 1, F = 0, R = 1, L = 0

class seat:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column
        self.ID = row * 8 + column

    def display(self):
        print("row:", self.row, "col:", self.column, "ID:", self.ID)



def part1():
    count = 0
    maxID = 0
    seats = []
    onlist = [0] * 1017


    with open('da5.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            column = line.lstrip('BF')
            column = int(column.replace('R', '1').replace('L', '0'), 2)
            row = line.rstrip('LR\n')
            row = int(row.replace('B', '1').replace('F', '0'), 2)
            ticket = seat(row, column)
            seats.append(ticket)
            ID = row * 8 + column
            onlist[ID] += 1
            if(ID > maxID):
                maxID = ID
    for i in range(0,1017):
        if onlist[i] == 0 and onlist[i-1] != 0 and onlist[i+1] != 0:
            print(i)
    return maxID


print(part1())
