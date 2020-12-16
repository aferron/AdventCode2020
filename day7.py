# advent of code 2020
# day 7
# which colors of bags can hold a gold bag?
# it's a directed graph

#make a class to contain connection info
class bag:
    def __init__(self, color='', contains=[], visited=False):
        self.color = color
        self.contains = contains
        self.visited = visited

    def display(self):
        print(self.color, "->", end='\n')
        for c in self.contains:
            c.display()
            print()

class edge:
    def __init__(self, weight=0, color=''):
        self.weight = weight
        self.color = color

    def display(self):
        print('#:', self.weight, end=' ')
        print("color:", self.color, end=' ')

def readin():
    count = 0
    readLines = []
    keyVals = {}

    with open('da7.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            # remove the \n at end of line
            line1 = line.strip()
            # separate containing bags from contained, removing ' bags '
            line2 = line.split(' bags ')
            # remove whitespace from containing bag
            line2[0] = line2[0].strip()
            # remove '.\n' from end, remove 'contain ' from beginning, split at ', '
            line2[1] = line2[1].strip('.\n').lstrip('contain ').split(', ')
            edgeList = []
            # now fix each of the contained bags
            for e in line2[1]:
                if "her bags" in e:
                    e = None
                else:
                    # remove 'bags' or 'bag'
                    e = e.removesuffix('s')
                    e = e.removesuffix('bag')
                    # separate number from color and get rid of leading or trailing whitespace
                    e = e.split(' ', 1)
                    e[0] = e[0].strip()
                    e[1] = e[1].strip()
                    # create an edge class instance with number and color
                    e = edge(int(e[0]), e[1])
                    print()
                    # add to edgeList
                    edgeList.append(e)
            line2[1] = edgeList
            add = bag(line2[0], line2[1], False)
            readLines.append(add)

        for r in readLines:
            r.display()

readin()

