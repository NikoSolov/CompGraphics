import os

s=0 # кол-во заглавных русских букв
e2=0 # кол-во "АБВГ"
eP=0 # кол-во П
eN=0 # кол-во Н
time2=0
state="" # состояния П или Н
string=""
f=open("ChELNOK_null_BP_exp6_my_Exp_VeraVlad_1_Rat_S2b.txt", "r",  encoding='utf-8')
fout=open("ChELNOK_null_BP_exp6_my_Exp_VeraVlad_1_Rat_S2b.txt__result.txt","w")
   
fout.write("time\tlength\tП\tН\t(АБВГ)\tstring\n")

for i in range(15):
    f.readline()

a=f.readline()
time=int(a[:a.find(":")+a.find('\t')+1])
    
while a!="":
    time2=int(a[:a.find(":")+a.find('\t')+1])
    sym=a[a.find(":")+a.find('\t')+1+1:][0]
    b=ord(sym)
    #print(a)
    if (b>1039 and b<1072 or b==1025 or sym=="+"):
        string+=sym
        s+=1
        if sym=="А" or sym=="Б" or sym=="В" or sym=="Г":
            print(sym)
            e2+=1
    
    if sym=="П": eP+=1
    if sym=="Н": eN+=1
    
    if sym=="П" or sym=="Н":
        if state=="": state=sym
        elif state!=sym:
            if sym=="Н":
                fout.write(str(int(a[:a.find(":")+a.find('\t')+1])-time))
                fout.write('\t')
                fout.write(str(s)+'\t'+str(eP)+'\t'+str(eN)+'\t'+str(e2)+'\t'+str(string)+'\n')
                #print("Итог:",s)
                time=int(a[:a.find(":")+a.find('\t')+1])
                s=eP=eN=e2=0
                string=""
            state=sym
    a=f.readline()


fout.write(str(time2-time)+'\t'+str(s)+'\t'+str(eP)+'\t'+str(eN)+'\t'+str(e2)+'\t'+str(string))
f.close()
fout.close()
