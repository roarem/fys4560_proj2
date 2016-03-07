inFile = open("lgrng11.mdl",'r')

#inFile.readline()
#inFile.readline()
#inFile.readline()

ZpEntries = []
original  = []
Z = 'Z'
Zp = 'Zp'

for i,line in enumerate(inFile):
    original.append(line)
    if i>2:
        if Z in line:

            Zline = line.split(Z)
            nZ = len(Zline) 
            if  nZ == 2:
                tempZp = Zline[0]+Zp+Zline[1]    
                ZpEntries.append(tempZp)

            elif nZ == 3:
                tempZp = Zline[0]+Zp+Zline[1]+Z+Zline[2]
                ZpEntries.append(tempZp)
                tempZp = Zline[0]+Zp+Zline[1]+Zp+Zline[2]
                ZpEntries.append(tempZp)

            elif len(Zline) == 4:
                tempZp = Zline[0]+Zp+Zline[1]+Z+Zline[2]+Z+Zline[3]
                ZpEntries.append(tempZp)
                tempZp = Zline[0]+Zp+Zline[1]+Zp+Zline[2]+Z+Zline[3]
                ZpEntries.append(tempZp)
                tempZp = Zline[0]+Zp+Zline[1]+Zp+Zline[2]+Zp+Zline[3]
                ZpEntries.append(tempZp)

            elif len(Zline) == 5:

                tempZp = Zline[0]+Zp+Zline[1]+Z+Zline[2]+Z+Zline[3]+Z+Zline[4]
                ZpEntries.append(tempZp)
                tempZp = Zline[0]+Zp+Zline[1]+Zp+Zline[2]+Z+Zline[3]+Z+Zline[4]
                ZpEntries.append(tempZp)
                tempZp = Zline[0]+Zp+Zline[1]+Zp+Zline[2]+Zp+Zline[3]+Z+Zline[4]
                ZpEntries.append(tempZp)
                tempZp = Zline[0]+Zp+Zline[1]+Zp+Zline[2]+Zp+Zline[3]+Zp+Zline[4]
                ZpEntries.append(tempZp)

    

inFile.close()
outFile = open("outFile",'w')
for entry in original[:-2]:
    outFile.write(str(entry)+'\n')

for entry in ZpEntries:
    outFile.write(str(entry)+'\n')

outFile.write(original[-1])
outFile.close()

