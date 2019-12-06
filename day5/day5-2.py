#!/usr/bin/python3


mass=open("input", "r")
i=0
run=1
for line in mass:
    a=line[0:len(line)-1].split(",")
a = [ int(x) for x in a ]
while i<len(a) and run == 1:
    op=a[i]%100
    A = (1 == int(a[i] /10000) %100) #immedate mode
    B = (1 == int(a[i] /1000) %10)
    C = (1 == int(a[i] /100) %2)
    print(a[i:i+4],A,B,C)
    if op == 99:
        #exit
        run=0
    else:
        if op == 8:
            #equals to
            if B == False:
                a[i+2] = a[a[i+2]]
            if C == False:
                a[i+1] = a[a[i+1]]
            if a[i+1] == a[i+2]:
                a[a[i+3]] = 0
            else:
                a[a[i+3]] = 1
            i+=4
        if op == 7:
            #less than
            if B == False:
                a[i+2] = a[a[i+2]]
            if C == False:
                a[i+1] = a[a[i+1]]
            if a[i+1] < a[i+2]:
                a[a[i+3]] = 0
            else:
                a[a[i+3]] = 1
            i+=4
        if op == 6:
            #jmp false
            if B == False:
                a[i+2] = a[a[i+2]]
            if C == False:
                a[i+1] = a[a[i+1]]
            if a[i+1] == 0:
                i = a[i+2]
            else:
                i+=3
        if op == 5:
            #jmp true
            if B == False:
                a[i+2] = a[a[i+2]]
            if C == False:
                a[i+1] = a[a[i+1]]
            if a[i+1] == 1:
                i = a[i+2]
            else:
                i+=3

        if op == 4:
            #output
            if C == True:
                print(a[i+1])
            else:
                print(a[a[i+1]])
            i+=2
        if op == 3:
            #input
            a[a[i+1]] = int(input('> '))
            i+=2
        if op == 2:
            #multiply
            if B == False:
                a[i+2] = a[a[i+2]]
            if C == False:
                a[i+1] = a[a[i+1]]
            a[a[i+3]] = a[i+1] * a[i+2]
            i+=4
        if op == 1:
            #add
            if B == False:
                a[i+2] = a[a[i+2]]
            if C == False:
                a[i+1] = a[a[i+1]]
            a[a[i+3]] = a[i+1] + a[i+2]
            i+=4
    #input()
