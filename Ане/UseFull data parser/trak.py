import os

mylist = os.listdir("Files")

for file in mylist:
    s=0 # кол-во заглавных русских букв
    c=0 # кол-во плюсов
    e2=0 # кол-во "АБВГ"
    e=0 # кол-во ошибок вида "ПП" "НН"
    time2=0
    state="" # состояния П или Н
    string=""
    print(file)
    f=open("Files//"+file, "r",  encoding='utf-8')
    fout=open("Results//"+file+"__result.txt","w")
    fout.write("time\tlength\t(ПП/НН)\t(АБВГ)\tstring\n")

    for i in range(15):
        f.readline()

    a=f.readline()
    time=int(a[:a.find(":")+a.find('\t')+1])
    while a!="":
        time2=int(a[:a.find(":")+a.find('\t')+1])
        sym=a[a.find(":")+a.find('\t')+1+1:][0]
        b=ord(sym)
        #print(a)
        if (b>1039 and b<1072 or b==1025):
            if sym=="A" or sym=="Б" or sym=="В" or sym=="Г":
                e2+=1
            if sym=="П" or sym=="Н":
                if state==sym:
                    e+=1
                state=sym
            string+=sym
            #print(a)
            s+=1
        elif sym=='+' and c==0:
            string+=sym
            #print(a)
            c=1
        elif sym=='+' and c==1:
            string+=sym
            #print(a)
            #print("time=", time,int(a[:a.find(":")+a.find('\t')+1])-time)
            fout.write(str(int(a[:a.find(":")+a.find('\t')+1])-time))
            fout.write('\t')
            
            fout.write(str(s)+'\t'+str(e)+'\t'+str(e2)+'\t'+str(string)+'\n')
            #print("Итог:",s)
            time=int(a[:a.find(":")+a.find('\t')+1])
            s=c=e2=e=0
            state=string=""

        a=f.readline()

    fout.write(str(time2-time)+'\t'+str(s)+'\t'+str(e)+'\t'+str(e2)+'\t'+str(string))
    f.close()
    fout.close()
