import sys
def part1(input):
    lines=getlines(input)
    gridx,gridy=findgridlength(lines)
    grid=getgrid(gridx,gridy)
    horizontal,vertical=gethorizontalandverticallines(lines)
    straightlines=horizontal+vertical
    grid=fillgrid(grid,straightlines)
    overlaps=getoverlaps(grid)
    return overlaps

def part2(input):
    lines=getlines(input)
    gridx,gridy=findgridlength(lines)
    grid=getgrid(gridx,gridy)
    grid=fillgrid(grid,lines)
    overlaps=getoverlaps(grid)
    return overlaps 

def getlines(input):
    lines=[]
    tonum=lambda x: int(x)
    for lin in input:
        a=lin.split(' ')
        startpoint=list(map(tonum,a[0].split(',')))
        endpoint=list(map(tonum,a[len(a)-1].split(',')))
        line=[]
        line.append(startpoint)
        line.append(endpoint)
        lines.append(line)
    return lines

def gethorizontalandverticallines(lines):
    horizontalLines=[]
    verticalLines=[]
    for line in lines:
        if(line[0][0]==line[1][0]):
            verticalLines.append(line)
        elif(line[0][1]==line[1][1]):
            horizontalLines.append(line)
    return horizontalLines,verticalLines


def findgridlength(lines):
    largestx=0
    largesty=0
    larger=lambda x,y: x if (x>=y) else y
    for line in lines:
        largestxinline=larger(line[0][0],line[1][0])
        largestx=larger(largestx,largestxinline)
        largestyinline=larger(line[0][1],line[1][1])
        largesty=larger(largesty,largestyinline)
    return largestx,largesty

def getgrid(x,y):
    # should be np array 
    grid=[]
    for a in range(0,y+1):
        row=[]
        for b in range(0,x+1):
            row.append(0)
        grid.append(row)
    return grid

def fillgrid(grid,lines):
    # need to use alternative strategy for looping or arrange points by size..former is better since it is a general approach.
    gridx=len(grid[0])-1
    gridy=len(grid)-1
    for lin in lines:
        line=makeLine(gridx,gridy,lin[0],lin[1])
        for point in line:
            grid[point[0]][point[1]]+=1
    return grid
def makeLine(gridx,gridy,p1,p2):
    line=[] # -> [p1,p2,[x3,y3]]
    xdiff = p1[0]-p2[0]
    ydiff = p1[1]-p2[1]
    ascend=lambda x,y: [x,y] if (x<y) else [y,x]
    if(xdiff == 0):
        y=ascend(p1[1],p2[1])
        curr_y=y[0]
        while(curr_y<=y[1]):
            line.append([p1[0],curr_y])
            curr_y+=1
    elif(ydiff==0):
        x=ascend(p1[0],p2[0])
        curr_x=x[0]
        while(curr_x<=x[1]):
            line.append([curr_x,p1[1]])
            curr_x+=1
    else:
        gradient=ydiff/xdiff
        getStart=lambda x,y: x if (x[0] < y[0]) else y;
        getEnd=lambda x,y: x if (x[0] > y[0]) else y;
        startpoint=getStart(p1,p2)
        endpoint=getEnd(p1,p2)
        curr_x=startpoint[0]
        curr_y=startpoint[1]
        while(curr_x<=endpoint[0]):
            line.append([curr_x,curr_y])
            curr_x+=1
            curr_y+=int(gradient)
    return line



def getoverlaps(grid):
    count=0
    for row in grid:
        for point in row:
            if(point>1):
                count+=1
    return count


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


