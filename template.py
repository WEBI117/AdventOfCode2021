import sys
def part1(input):
    print("Hello from part 1")
def part2(input):
    print ("Hello from part 2")

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


