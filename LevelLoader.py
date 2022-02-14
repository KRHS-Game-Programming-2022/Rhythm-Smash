from ArrowTile import*
from ArrowBox import*

#Will be fixed later; just basic code to read a file

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()



    size = 50
    speed = [0,2]
    arrows = []
    offset = size/2

    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newLines += [newline]

    lines = newLines

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "<":
                arrows += [ArrowTile("left", speed, [75, -100-(y*size*2+offset)])]
            elif c == "v":
                arrows += [ArrowTile("down", speed, [150, -100-(y*size*2+offset)])]
            elif c == "^":
                arrows += [ArrowTile("up", speed, [225, -100-(y*size*2+offset)])]
            elif c == ">":
                arrows += [ArrowTile("right", speed, [300, -100-(y*size*2+offset)])]

    return arrows

