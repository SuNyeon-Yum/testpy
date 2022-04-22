import os

f=open('mbox.txt')

fw=open('temp.txt','w')

for line in f :

    if line.startswith('From') :

        line=line.rstrip()

        t=line.split()

        if len(t)<=2 :

            continue

        print(t[1]+','+t[-1])

        fw.write(t[1]+','+t[-1]+'\n')

f.close()

fw.close()
