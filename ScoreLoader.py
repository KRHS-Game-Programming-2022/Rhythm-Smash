from ArrowTile import*
from ArrowBox import*

def loadScores(lev):
    f = open("Levels/scrs", 'r')
    lines = f.readlines()
    f.close()


    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newLines += [newline]
    lines = newLines

    newlines = []
    for line in lines:
        newLines += line.split(',')
    lines = newLines

    for line in lines:
        if line[0] == "lev":
            pass


