from ArrowTile import*
from ArrowBox import*

def loadScores(lev):
    f = open("Levels/" + lev+ ".scrs", 'r')
    lines = f.readlines()
    f.close()


    newLines = []
    for line in lines:
        newline = int(line);
        newLines += [newline]
    lines = newLines

    return lines


def saveScores(lev, scores):
    out = ""
    for score in scores:
        out += str(score)+"\n"

    f = open("Levels/" + lev+ ".scrs", 'w')
    lines = f.write(out)
    f.close()





