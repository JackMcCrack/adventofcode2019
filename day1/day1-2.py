#!/usr/bin/python3
total=0
mass=open("input.txt", "r")

for line in mass:
    fule=int(int(line)/3)-2
    more=0
    while(fule > 0):
        more+=fule
        fule=int(fule/3)-2

    total+=more
print(total)
