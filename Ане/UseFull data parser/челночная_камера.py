import os
mylist = os.listdir("Files_2")

for file in mylist:
    s=0 # кол-во заглавных русских букв
    c=0 # кол-во Ы
    flag=False
    e2=0 # кол-во "АБВГ"
    e=0 # кол-во ошибок вида "ПП" "НН"
    state="" # состояния П или Н
    string=""
    time2=0
    print(file)
    f=open("Files_2//"+file, "r",  encoding='utf-8')
    fout=open("Results_3//"+file+"__result.txt","w")
    fout.write("time\tlength\tt(/.Ы)\tc(Ы)\tstring\n")

    for i in range(15):
        f.readline()

    a=f.readline()
    time=int(a[:a.find(":")+a.find('\t')+1])
    while a!="":
        sym=a[a.find(":")+a.find('\t')+1+1:][0]
        b=ord(sym)
        #print(a)
        if ((b>1039 and b<1072) or b==1025 or (b>47 and b<58)):
            #print(a)
            s+=1
            string+=sym
            if sym=='Ы':
                #print(a[:a.find(":")+a.find('\t')+1])
                if flag==False:
                    time2=int(a[:a.find(":")+a.find('\t')+1])-time
                    flag=True
                else:
                    c+=1
        elif sym=="*" or sym=="-":
            string+=sym
        elif sym=='/':
            string+=sym
            #print(a)
            #print("time=", time,int(a[:a.find(":")+a.find('\t')+1])-time)
            fout.write(str(int(a[:a.find(":")+a.find('\t')+1])-time))
            fout.write('\t')
            
            fout.write(str(s)+'\t'+str(time2)+'\t'+str(c)+'\t'+str(string)+'\n')
            #print("Итог:",s)
            time=int(a[:a.find(":")+a.find('\t')+1])
            string=""
            s=0
            time2=0
            c=0
            flag=False
        a=f.readline()

    fout.write(str(time)+'\t'+str(s)+'\t'+str(time2)+'\t'+str(c)+'\t'+str(string)+'\n')
    f.close()
    fout.close()
