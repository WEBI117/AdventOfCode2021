import sys
def part1(input):
    ages=getAges(input)
    print(ages)
def part2(input):
    print ("Hello from part 2")

def getAges(lines):
    for x in lines:
        return list(map(lambda x: int(x),x.split(',')))
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


