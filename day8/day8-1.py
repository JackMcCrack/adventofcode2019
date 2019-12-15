#!/usr/bin/python3

sizex=6
sizey=25

count = []

inputfile=open("input", "r")
for line in inputfile:
    layer = -1
    i = 0
    while i < len(line)-1:
        if (i%(sizex*sizey)==0):
            layer += 1
            count.append([])
            for j in range(10):
                count[layer].append([])
                count[layer][j]=0
        count[layer][int(line[i])] += 1
        i += 1

maxzero=99
lowest=[]
for layer in count:
    if layer[0]<maxzero:
        maxzero = layer[0]
        lowest = layer

print(lowest, lowest[1]*lowest[2])
