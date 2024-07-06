import os


if os.path.isdir("files")==False:
 os.mkdir("files")
 input("Папка 'files' создана.\nПоложи в нее файлы лога и запусти программу снова\nPress any keyboard key to exit program.")
 quit()

direc = os.listdir("files")

task=[]
mouse=[]

mouse_row = int(input("Введи номер столбца для 'Мышей': "))-1
tasks_row = int(input("Введи номер столбца для 'Задачек': "))-1
#print(mouse_row, tasks_row)

for i in direc:            # перечисляем файлы
 file=open("files//"+i)
 if "Tasks" in i:
  a=[]
  for j in file:           # считываем файлы по строкам
   c = j.split("\t")
   if "" in c: c.remove("")
   a.append(c)
  task.append([ j[tasks_row].replace("\n","") for j in a[1:-3] ])


 else:
  a=[]
  for j in file:
   c = j.split("\t")
   if "" in c: c.remove("")
   a.append(c)
  mouse.append([j[mouse_row].replace("\n","") for j in a[4:]])
 file.close()



b_zip=zip(*task)
file=open("Tasks_result.txt", "w") 
for i in b_zip:
 for j in i:
  file.write(j+"\t")
 file.write("\n")
file.close()


c_zip=zip(*mouse)
file=open("Mouses_result.txt", "w")
for i in c_zip:
 for j in i:
  file.write(j+"\t")
 file.write("\n")
file.close()

input("Все готово!!!\nPress any keyboard key to exit program.")
#for i in range(length(b))
