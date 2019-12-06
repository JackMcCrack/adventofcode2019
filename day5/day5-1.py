#!/usr/bin/python3

mass=open("input", "r")
i=0
run=1
for line in mass:
    a=line.split(",")
a = [ int(x) for x in a ]
while i<len(a) and run == 1:
    op=a[i]%100
    A = (1 == int(a[i]/10000)%100) #immedate mode
    B = (1 == int(a[i]/1000)%10)
    C = (1 == int(a[i]/100)%2)
    print(a[i:i+4])
    if op == 99:
        #exit
        run=0
    
    else:
        if op == 4:
            #output
            print(a[i+1])
            i+=2
        if op == 3:
            #input
            a[a[i+1]]=int(input('> '))
            i+=2
        if op == 2:
            #multiply
            a[a[i+3]]=a[i+1]*a[i+2]
            i+=4
        if op == 1:
            #add
            a[a[i+3]]=a[i+1]+a[i+2]
            i+=4
    input()
