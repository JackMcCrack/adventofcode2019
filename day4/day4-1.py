#!/usr/bin/python3
inp=[347312,805915]
count = 0
for x in range(inp[0],inp[1]):
    dupl = False
    xa = [int(i) for i in str(x)]
    for pos in range(5,0,-1):
        for chkpos in range(pos-1,-1,-1):
            #print(pos,chkpos)
            if xa[pos] == xa[chkpos]:
                dupl = True
        if xa[pos-1] > xa[pos]:
            break
        if pos == 1 and dupl == True:
            print(x)
            count += 1

print(count)



    
