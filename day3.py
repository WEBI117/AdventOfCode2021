import sys

def part1(input):
    length = len(input);
    indexCounts = []
    for x in range(0,len(input[0])):
        indexCounts.append(0);
    for x in input:
        for y in range(0,len(x)):
            if(x[y] == '0'):
                indexCounts[y] -= 1;
            else:
                indexCounts[y] += 1;
    gamma = extractNum(indexCounts);
    epsilon = getOpposite(gamma);
    return int(gamma,2) * int(epsilon,2);

def part2(input):
    stopind = len(input[0])-1;
    O2 = recursiveSolve2(input,0,True);
    CO2 = recursiveSolve2(input,0,False);
    return int(O2,2) * int(CO2,2);

def recursiveSolve2(array, currindex, o2):
    # assuming we never run into a situation where all the entries in an array at the currindex have the same value... 
    if(len(array) == 1):
        return array[0];
    ones = []
    zeros = []
    for x in array:
        if(x[currindex] == '0'):
            zeros.append(x)
        else:
            ones.append(x)
    if(o2):
        newarr = getLarger(ones,zeros);
        return recursiveSolve2(newarr,currindex+1,o2)
    else:
        newarr = getSmaller(ones,zeros);
        return recursiveSolve2(newarr,currindex+1,o2)
def getLarger(ones,zeros):
    len1 = len(ones)
    len2 = len(zeros)
    if(len1>=len2):
        return ones
    else:
        return zeros
def getSmaller(ones,zeros):
    len1 = len(ones)
    len2 = len(zeros)
    if(len1<len2):
        return ones
    else:
        return zeros

# incorrect solution....the entries in the array may be exhausted before all the indexes have been itrated over.
def recursiveSolve(checkchar, currindex, array, stopindex, O2):
    # checkchar is the opposite character to what we return in previous recursive call....
    print(array)
    print('----')
    newarr = []
    indexCounts = 0
    if(currindex > stopindex):
        return '';
    else:
        for x in array:
            if(currindex != 0):
                if(x[currindex - 1]!=checkchar):
                    newarr.append(x);
                    if(x[currindex] == '0'):
                        indexCounts -= 1;
                    else:
                        indexCounts += 1;
            else:
                newarr.append(x);
                if(x[currindex] == '0'):
                    indexCounts -= 1;
                else:
                    indexCounts += 1;

        if O2:
            if(indexCounts < 0):
                return '0' + recursiveSolve('1', currindex + 1, newarr, stopindex, O2)
            else:
                return '1' + recursiveSolve('0', currindex + 1, newarr, stopindex, O2)
        else:
            if(indexCounts < 0):
                return '1' + recursiveSolve('0', currindex + 1, newarr, stopindex, O2)
            else:
                return '0' + recursiveSolve('1', currindex + 1, newarr, stopindex, O2)
def extractNum(arr):
    binarystring = ""
    for x in arr:
        if(x < 0):
            binarystring += '0';
        else:
            binarystring += '1';
    return binarystring;
def getOpposite(binaryString):
    binarystring = ""
    for x in binaryString:
        if(x == '0'):
            binarystring += '1';
        else:
            binarystring += '0';
    return binarystring;


def readfile(filename):
    fileStream=open(filename,"r");
    lines = fileStream.read();
    lines = lines.split('\n')[:-1];
    fileStream.close();
    return lines
if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Please provide the correct number of command line arguments...");
        print(f"Expected 2 but got {len(sys.argv) - 1}");
        exit();
    filename = sys.argv[1]
    part = sys.argv[2]
    lines = readfile(filename)
    if(part == "1"):
        print(part1(lines))
    elif(part == "2"):
        print(part2(lines))
    else:
        print("Incorrect part.")


