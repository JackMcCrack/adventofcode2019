#!/usr/bin/python3
inp=[347312,805915]
count = 0
for x in range(inp[0],inp[1]):
    inc = True
    cnt = []
    xa = [int(i) for i in str(x)]
    dig = set(xa)
    for pos in range(5,0,-1):
        if xa[pos-1] > xa[pos]:
            inc = False

    for x in dig:
        y=0
        for pos in range(6):
            if xa[pos] == x:
                y += 1
        cnt.append(y)
    if 2 in cnt and inc == True:
        count += 1
                
print(count)



    
