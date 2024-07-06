file="Проша_new.txt"
fin=open(file, "r")
fout=open("res4/"+file, "w")
def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0 


fout.write("Полож\tМедДо\tМедПос\n")
for i in range(1,6):
    before=[]
    after=[]
    fin.seek(0)
    fin.readline()
    a=fin.readline()
    while a!="":
        b=a.split("\t")
        #print(b)
        if b[6]==str(i):
            if b[8]!="\n" and b[8]!="":
                if int(b[2])==1: before.append(float(b[1]))
                if int(b[2])==2: after.append(float(b[1]))
        a=fin.readline()
        #print(before,median(before))

    fout.write(str(i)+"\t"+str(median(before))+"\t"+str(median(after)))
    fout.write("\n")
            
fout.close()
fin.close()
