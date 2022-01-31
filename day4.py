import sys
import numpy as np

def part1(input):
    calls = input[0].split(',')
    tables = gettables(input)
    tablescopy = tables
    for num in calls:
        for index,table in enumerate(tables):
            tables[index] = marktable(table,num)
            if(Bingo(table)):
                print(table)
                return 
                #return getResult(table,num)
    #print(tables)

def part2(input):
    print ("Hello from part 2")

def marktable(table,number):
    for index, row in enumerate(table):
        markedrow = list(map(lambda x: 'm' if (x == number) else x, row))
        table[index] = markedrow
    return table

def Bingo(table):
    table = np.array(table)
    colLen = len(table)
    rowLen = len(table[0])
    for row in table:
        if(arrayMarked(row)):
            return True
    for x in range(0,colLen):
        col = table[x,:]
        if(arrayMarked(col)):
            return True

    return False

def getResult():
    return True;

def arrayMarked(array):
    return all(map(lambda x: True if (x == 'm') else False, array))

def gettables(input):
    tables = []
    currentTable = []
    for x in range(1,len(input)+1):
        if(x > len(input)-1 or input[x] == ''):
            if(len(currentTable) > 0):
                tables.append(currentTable)
                currentTable = []
        else:
            currentTable.append(list(filter(lambda x : True if (x != '') else False, input[x].split(' '))))

    return tables

def readfile(filename):
    fileStream=open(filename,"r")
    lines = fileStream.read()
    lines = lines.split('\n')[:-1]
    fileStream.close()
    return lines
if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Please provide the correct number of command line arguments...")
        print(f"Expected 2 but got {len(sys.argv) - 1}")
        exit()
    filename = sys.argv[1]
    part = sys.argv[2]
    lines = readfile(filename)
    if(part == "1"):
        print(part1(lines))
    elif(part == "2"):
        print(part2(lines))
    else:
        print("Incorrect part.")


