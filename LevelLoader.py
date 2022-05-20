from ArrowTile import *
from ArrowBox import *


def loadLevel(lev, players=1):
    f = open(lev + ".lvl", 'r')
    lines = f.readlines()
    f.close()

    bpm = int(lines[0])
    lines.remove(lines[0])
    bps = bpm / 60

    difficulty = float(lines[0])
    lines.remove(lines[0])
    pps = bps * difficulty

    size = 50
    speed = [0, pps]
    arrows = []
    offset = size / 2

    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newLines += [newline]

    lines = newLines

    if players == 1:
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "<":
                    arrows += [ArrowTile("left", speed, [75, -100 - (y * size * 2 + offset)])]
                    print("p1: ", arrows[-1])
                elif c == "v":
                    arrows += [ArrowTile("down", speed, [150, -100 - (y * size * 2 + offset)])]
                elif c == "^":
                    arrows += [ArrowTile("up", speed, [225, -100 - (y * size * 2 + offset)])]
                elif c == ">":
                    arrows += [ArrowTile("right", speed, [300, -100 - (y * size * 2 + offset)])]


    if players == 2:
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "<":
                    arrows += [ArrowTile("left", speed, [900-300, -100 - (y * size * 2 + offset)])]
                    print("p2: ", arrows[-1])
                elif c == "v":
                    arrows += [ArrowTile("down", speed, [900-225, -100 - (y * size * 2 + offset)])]
                elif c == "^":
                    arrows += [ArrowTile("up", speed, [900-150, -100 - (y * size * 2 + offset)])]
                elif c == ">":
                    arrows += [ArrowTile("right", speed, [900-75, -100 - (y * size * 2 + offset)])]

    return arrows
