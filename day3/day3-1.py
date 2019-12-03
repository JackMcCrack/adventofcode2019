#!/usr/bin/python3
mass=open("input", "r")
direction = {'R': (1,0), 'D': (0,-1), 'L': (-1,0), 'U': (0,1)}
start = (0,0)
trace = []
intersection = []

first=True
for line in mass:
    a = line.split(",")
    pos = start
    for i in a:
        d = i[0]
        count = int(i[1:])
        (stpx, stpy) = direction.get(d, (0,0))
        for x in range(count):
            pos = (pos[0]+stpx, pos[1]+stpy)
            if first:
                trace.append(pos)
            else:
                if pos in trace:
                    print(pos)
                    intersection.append(pos)
    first=False
