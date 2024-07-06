file="Проша_new.txt"
fin=open(file, "r")
fout=open("res3/"+file, "w")
def median(lst):
    n = len(lst) if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0 


fout.write("Полож\t\Рук'0'\tРук'0'%\tРук'1'\tРук'1'%\t\n")
for i in range(1,6):
    lst=[]
    hand0=hand1=hand=0
    fin.seek(0)
    fin.readline()
    a=fin.readline()
    while a!="":
        b=a.split("\t")
        #print(b)
        if b[6]==str(i):
            if b[8]!="\n" and b[8]!="":
                if int(b[8])==0: hand0+=1
                if int(b[8])==1: hand1+=1
                hand+=1
            lst.append(int(b[1]))
        a=fin.readline()

    fout.write(str(i)+"\t")
    fout.write(str(hand0)+"\t"+str(round(hand0/hand*100))+"\t")
    fout.write(str(hand1)+"\t"+str(round(hand1/hand*100))+"\t")
    fout.write("\n")
            
fout.close()
fin.close()
