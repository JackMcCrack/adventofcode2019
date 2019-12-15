#!/usr/bin/python3

sizex=6
sizey=25

out=[]
for x in range(sizex*sizey):
    out.append('2')
layer=[]
inputfile=open("input", "r")
for line in inputfile:
    i = 0
    while i < len(line)-1:
        if (i%(sizex*sizey)==0):
            layer.append(line[i:i+sizex*sizey])
        i += sizex*sizey
for l in layer:
    i = 0
    while i < len(l):
        if out[i] == '2':
            out[i] = l[i]
        i += 1

for x in range(sizex):
    p = ''
    for y in (out[0+(x*sizey):sizey+(x*sizey)]):
        if y == '0':
            p += ' '
        if y == '1':
            p += '#'
    print(p)


