import sys
def part1(input):
    length = len(input);
    forwardposition = 0
    verticalposition = 0

    for x in input:
        line = x.split(' ');
        direction = line[0];
        magnitude = line[1];
        if(direction == "forward"):
            forwardposition += int(magnitude);
        elif(direction == "up"):
            verticalposition -= int(magnitude);
        elif(direction == "down"):
            verticalposition += int(magnitude);
    return forwardposition * verticalposition


def part2(input):
    aim = 0
    horizontalposition = 0
    verticalposition = 0
    for x in input:
        line = x.split(' ');
        direction = line[0];
        magnitude = line[1];
        if(direction == "down"):
            aim += int(magnitude);
        elif(direction == "up"):
            aim -= int(magnitude);
        elif(direction == "forward"):
            horizontalposition += int(magnitude);
            verticalposition += aim*(int(magnitude));
    return horizontalposition*verticalposition;

            



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


