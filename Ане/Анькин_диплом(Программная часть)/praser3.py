file="Проша_new.txt"
fin=open(file, "r")
fout=open("res2/"+file, "w")

kontr0=0
kontr=0
obl0=0
obl=0

fout.write("Полож\tК'0'\tК'0'%\tОб'0'\tОб'0'%\t\n")
for i in range(1,6):
    kontr0=kontr=obl0=obl=0
    fin.seek(0)
    fin.readline()
    a=fin.readline()
    while a!="":
        b=a.split("\t")
        if b[6]==str(i):
            if b[2]=="1":
                if b[0]=="0": kontr0+=1
                kontr+=1
            if b[2]=="2":
                if b[0]=="0": obl0+=1
                obl+=1
        a=fin.readline()
        
    fout.write(str(i)+"\t")
    fout.write(str(kontr0)+"\t"+str(round(kontr0/kontr*100))+"\t")
    fout.write(str(obl0)+"\t"+str(round(obl0/obl*100))+"\t")
    fout.write("\n")
            
fout.close()
fin.close()
