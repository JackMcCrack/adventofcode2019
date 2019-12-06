#!/usr/bin/python3
orb=open("input", "r")
al = []
o = {}
t = {}
root = ''
for line in orb:
    a = line[0:len(line)-1].split(")")
    al.append(a[0])
    al.append(a[1])
    if a[0] in o:
        o[a[0]] += ','+a[1]
    else:
        o[a[0]] = a[1]
al = (set(al))
for x in al:
    l=0
    for i,j in o.items():
        if x in j:
            l=len(j)
#    if x in o:
#        print(x,len(o[x]),o[x])
#    else:
#        print(x,'0','')
    if (l == 0):
        root = x
print('root:',root)

t[0] = root
t[1] = o[root]
z = 1
while (len(al) > 0 and z in t ):
    z += 1
    
    for i in t[z-1].split(','):
        if i in o: 
            if z in t:
                t[z] += ','+o[i]
            else:
                t[z] = o[i]
            al.remove(i)
    #print(al,t,len(al),len(t))
orbits = 0
for i,j in t.items():
    print(i,len(j.split(',')))
    orbits += (i * len(j.split(',')))
print(orbits)
