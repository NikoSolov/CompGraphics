file="Ероша.txt"
fin=open(file, "r")
fout=open("res/"+file, "w")

day=1
err0=0
err1=0
err2=0
hand0=0
hand1=0
mode=1
fout.write("К/об\tДень\tОшибки\t\t\t\t\t\tРуки\n")
fout.write("\t\t'0'\t'0'%\t'1'\t'1'%\t'2'\t'2'%\t'0'\t'0'%\t'1'\t'1'%\n")
fin.readline()
a=fin.readline()
while a!="":
    b=a.split("\t")
    print(b)
    if day==int(b[3]):
        if b[0]!="" and b[0]!="\n":
            if int(b[0])==0: err0+=1
            if int(b[0])==1: err1+=1
            if int(b[0])==2: err2+=1
        if b[6]!="" and b[6]!="\n":    
            if int(b[6])==0: hand0+=1
            if int(b[6])==1: hand1+=1
        mode=b[2]
        #print(mode)
    else:      
        fout.write(str(mode)+"\t"+str(day)+"\t")
        fout.write(str(err0)+"\t"+str(round(err0/(err0+err1+err2)*100))+"\t")
        fout.write(str(err1)+"\t"+str(round(err1/(err0+err1+err2)*100))+"\t")
        fout.write(str(err2)+"\t"+str(round(err2/(err0+err1+err2)*100))+"\t")
        fout.write(str(hand0)+"\t"+str(round(hand0/(hand1+hand0)*100))+"\t")
        fout.write(str(hand1)+"\t"+str(round(hand1/(hand1+hand0)*100))+"\t")
        fout.write("\n")
        err0=err1=err2=hand0=hand1=0
        day=int(b[3])
    a=fin.readline()
fout.close()
fin.close()
