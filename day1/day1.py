#!/usr/bin/python3
total=0
mass=open("input.txt", "r")

for line in mass:
    total+=int(int(line)/3)-2
    print(total)
