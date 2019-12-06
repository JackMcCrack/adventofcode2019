#!/usr/bin/python3
n=0
v=0
out=0

mass=open("input", "r")
i=0
run=1
for line in mass:
    a=line.split(",")
a = [ int(x) for x in a ]
a[1]=n
a[2]=v
while i<len(a) and run == 1:
    op=a[i]%100
    A = (1 == int(a[i]/10000)%100)
    B = (1 == int(a[i]/1000)%10)
    C = (1 == int(a[i]/100)%2)
    #print(a[i:i+4])
    step=(a[i:i+4])
    step[0]=op
    
    #pos mode
    if A==False:
        step[3]=a[step[3]]
    if B==False:
        step[2]=a[step[2]]
    if C==False:
        step[1]=a[step[1]]
    if op == 99:
        #exit
        run=0
    
    else:
        if op == 4:
            #output
            print(step[1])
            i+=2
        if op == 3:
            #input
            if A==False:
                print(i,op)
                a[step[1]]=int(input('> '))

            i+=2
        if op == 2:
            #multiply
            if A==False:
                a[step[3]]=step[1]*step[2]
            i+=4
        if op == 1:
            #add
            if A==False:
                a[step[3]]=step[1]+step[2]
            i+=4
    print(i,op)
    sleep(10)
