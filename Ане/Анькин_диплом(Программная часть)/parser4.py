file="Жак.txt"
fin=open(file, "r")
fout=open("res2/"+file, "w")

fout.write("Полож\tErr'0'\tErr'0'%\n")
for i in range(1,6):
    err0=err=0
    fin.seek(0)
    fin.readline()
    a=fin.readline()
    while a!="":
        b=a.split("\t")
        if b[3]==str(i):
            if b[0]=="0": err0+=1
            err+=1
        a=fin.readline()
        
    fout.write(str(i)+"\t")
    fout.write(str(err0)+"\t"+str(round(err0/err*100))+"\t")
    fout.write("\n")
            
fout.close()
fin.close()
