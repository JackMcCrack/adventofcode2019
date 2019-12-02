#!/usr/bin/python3
mass=open("input", "r")
i=0
run=1
for line in mass:
    a=line.split(",")
a = [ int(x) for x in a ]
a[1]=12
a[2]=2
while i<len(a) and run == 1:
    #print(a[i:i+4])
    step=(a[i:i+4])
    if step[0] == 99:
        run=0
    else:
        if step[0] == 2:
            #multiply
            a[step[3]]=a[step[1]]*a[step[2]]
        if int(step[0]) == 1:
            #add
            a[step[3]]=a[step[1]]+a[step[2]]
        
    i+=4

print(a[0])
