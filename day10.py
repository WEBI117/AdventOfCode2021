import sys

def part1(input):
    listopen=["(","<","[","{"]
    listclose=[")",">","]","}"]
    scorelist=[3,25137,57,1197]

    """
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.
    """
    total=0
    for str in input:
        score=getRecursiveScore([],str,listopen,listclose,scorelist)
        if score == -1:
            total+=0
        else:
            total+=score
    return total

def part2(input):
    listopen=["(","<","[","{"]
    listclose=[")",">","]","}"]
    scorelist=[1,4,2,3]

    """
    ): 1 point.
    ]: 2 points.
    }: 3 points.
    >: 4 points.
    """
    scores=[]
    for str in input:
        missingcharlist=recuresiveGetOpenChars([],str,listopen,listclose)
        if missingcharlist[0] != '.':
            score=getmissingcharscore(reversed(missingcharlist),listopen,scorelist)
            scores.append(score)
    sortedscores=sorted(scores)
    return sortedscores[len(sortedscores)//2]

def getmissingcharscore(openchars,charlist,scorelist):
    score=0
    for char in openchars:
        score*=5
        score+=scorelist[charlist.index(char)]
    return score

def getRecursiveScore(listopen,str,openchars,closechars,scorelist):
    # modified to include and check for len of listopen to identify incomplete string.
    if len(str)==0:
        if len(listopen) == 0:
            #complete
            return 0
        else:
            #incomplete
            return -1

    remainingstr=str[1:]
    currchar=str[0]

    if currchar in openchars:
        listopen.append(currchar)
        return getRecursiveScore(listopen,remainingstr,openchars,closechars,scorelist)
    else:
        if openchars.index(listopen[-1]) != closechars.index(currchar):
            return scorelist[closechars.index(currchar)]
        else:
            return getRecursiveScore(listopen[:-1],remainingstr,openchars,closechars,scorelist)
    
def recuresiveGetOpenChars(listopen,str,openchars,closechars):
    if len(str)==0:
        if len(listopen)==0:
            return []
        else:
            return listopen

    remainingstr=str[1:]
    currchar=str[0]

    if currchar in openchars:
        listopen.append(currchar)
        return recuresiveGetOpenChars(listopen,remainingstr,openchars,closechars)
    else:
        if openchars.index(listopen[-1]) != closechars.index(currchar):
            return ['.']
        else:
            return recuresiveGetOpenChars(listopen[:-1],remainingstr,openchars,closechars)

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


