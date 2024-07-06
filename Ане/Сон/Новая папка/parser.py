import os
if os.path.isdir('data_input')==False:
    os.mkdir('data_input')
input("Положите файлы в папку 'data_input' и \n\nНажмите ENTER для продолжения\n")
if os.path.isdir('result')==False:
    os.mkdir('result')
a=input("Отображать лог?(y/n)(n - default): ")
log=False
if a=="y": log=True
sep=" "

mylist = os.listdir("data_input")
for file in mylist:
    if log==True: print("Обработка", file," ...", end="")
    ifile=open("data_input//"+file,"r",encoding='utf-8')
    ofile=open("result//"+file[:-4]+"!!!!.txt","w",encoding='utf-8')
    for i in ifile:    
        a=i.split(" ")
        #print(a)
        for i in range(len(a)):
            if a[i]=="Range:":
                ofile.write(str(a[i+1])+sep)
                break
        ifile.readline()
        a=ifile.readline().split()
        for i in range(1,len(a)):
            ofile.write(str(a[i])+sep)
    ifile.close()
    ofile.close()
    if log==True: print("DONE!")
print("\nОбработано",len(mylist),"файла(-ов) в папку result\n")
input("Нажмите ENTER для завершения программы")


    
