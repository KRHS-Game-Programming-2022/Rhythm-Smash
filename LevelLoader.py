from ArrowTile import*
from ArrowBox import*

def loadLevel(lev):
    f = open(lev+".lvl", 'r')
    lines = f.readlines()
    f.close()

    bpm = int(lines[0])
    lines.remove(lines[0])
    bps = bpm / 60

    difficulty = float(lines[0])
    lines.remove(lines[0])
    pps = bps * difficulty


    size = 50
    speed = [0,pps]
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

