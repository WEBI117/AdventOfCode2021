import sys

def part1(input):
    counts = 0;
    for x in range(1,len(input)):
        if(int(input[x-1]) < int(input[x])):
            counts += 1
    return counts;

def part2(input):
    previousDepth = getWindowDepth(input,0);
    count = 0

    for x in range(1,len(input)):
        depth = getWindowDepth(input,x)
        if(depth == -1):
            break;
        if(previousDepth < depth):
            count += 1;
        previousDepth = depth
    return count;

def getWindowDepth(input, index):
    length = len(input);
    if(index+3 > length):
        return -1;
    else:
        depth = int(input[index])+int(input[index+1])+int(input[index+2]) 
        return depth;

# recursion stack limit exceeded....cannot use this recursive implementation.
def recursiveSolve(input, index, previousDepth):
    length = len(input)
    print(length, index)
    if(index + 3 > length):
        return 0;
    depth = int(input[index])+int(input[index+1])+int(input[index+2]) 
    if(depth > previousDepth):
        return 1 + recursiveSolve(input,index+1,depth);
    else:
        return 0 + recursiveSolve(input,index+1,depth);

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
       print(part1(lines));
    elif(part == "2"):
        print(part2(lines));
    else:
        print("Incorrect part.")


