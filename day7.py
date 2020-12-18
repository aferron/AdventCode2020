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
        self.pathtogold = False

    def display(self):
        print(self.color, "->", end='\n')
        if not self.contains:
            print("no bags")
        else:
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

def readIn():
    count = 0
    readLines = []
    keyVals = []

    with open('da7.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            # remove the \n at end of line
            line1 = line.strip()
            # separate containing bags from contained, removing ' bags '
            line2 = line.split(' bags ')
            # remove whitespace from containing bag
            line2[0] = line2[0].strip()
            # add containing bag to tuple list for dictionary
            keyVals.append((line2[0], count))
            # remove '.\n' from end, remove 'contain ' from beginning, split at ', '
            line2[1] = line2[1].strip('.\n').lstrip('contain ').split(', ')
            edgeList = []
            # now fix each of the contained bags
            for e in line2[1]:
                if "her bags" in e:
                    e = None
                else:
                    # remove 'bags' or 'bag'
                    e = e.rstrip('s')
                    e = e.rstrip('bag')
                    # separate number from color and get rid of leading or trailing whitespace
                    e = e.split(' ', 1)
                    e[0] = e[0].strip()
                    e[1] = e[1].strip()
                    # create an edge class instance with number and color
                    e = edge(int(e[0]), e[1])
                    # add to edgeList
                    edgeList.append(e)
            line2[1] = edgeList
            add = bag(line2[0], line2[1], False)
            readLines.append(add)
            count += 1
        keyValues = dict(keyVals)

    return (readLines, keyValues)

def depthFirst(graph):
    # get the adjacency list
    adjList = graph[0]
    # get the dictionary
    lookUp = graph[1]
    # just work with first item for now
    first = adjList[0]
    # keep track of which vertices are on the path to the gold bag
    goldset = set()

    for i in adjList:
        dive(lookUp, adjList, goldset, i)
    print("goldset: ", goldset)
    return len(goldset)

def dive(lookUp, adjList, goldset, vertex):
    goldpath = False
    #if vertex.visited is True:
        #print("V ", end='')
    #vertex.display()
    #print()
    # if the edge list is empty we can return
    if not vertex.contains:
        vertex.visited = True
        return False 
    # if we're at gold celebrate
    if vertex.color == "shiny gold":
        print("*****GOLD*****")
        return True
    # if we've already been here return whether we're on the right path
    if vertex.visited is True:
        if vertex.pathtogold is True:
            return True
        else:
            return False 

    # note that we've been here
    vertex.visited = True
    # loop through list with recursive call
    for node in vertex.contains:
        #lookup node.color in dictionary for index number
        goldpath = goldpath or dive(lookUp, adjList, goldset, adjList[lookUp[node.color]])
        #print(vertex.color, end=' ')
        if goldpath is True:
            # mark that we're on the path, and add to set on the path
            vertex.pathtogold = True
            print(vertex.color, " contains shiny gold")
            # Add to set that is on the path
            goldset.add(vertex.color)
            #print("(contains gold)")
    return goldpath






graph = readIn()
print(depthFirst(graph))
