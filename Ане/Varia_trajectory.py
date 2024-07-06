from os import listdir
import pathlib
import pandas as pd



# import sys
# original_stdout = sys.stdout
# out_file = open("out.csv", 'w')
# sys.stdout = out_file

alphabet = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя+')




files = [f for f in listdir(pathlib.Path().absolute()) if "ЧЕЛНОК" in f ]

all_kk = []
day_lines =[]
for f in files:   
    print(f,end = ',')
    
    log_file = open(f, 'r', encoding = 'utf-8')
    log_date = log_file.readline()
    log_time = log_file.readline()
    log_file.readline()
    log_exp = log_file.readline()
    log_file.readline()
    log_name = log_file.readline()
    for i in range(9):
        string = log_file.readline()
    string = "1"
    all_actions = ""
    while(string != ""):
        string = log_file.readline()
        if(string == ""):
            break
        time = int(string.split(":")[0])
        action = string.split(":")[1][0]
        if action in alphabet:
            all_actions += action
    print(all_actions)
    otv1 = all_actions.split('+')
    #посчитать длину проб. уже нормальных проб, не половинок
    Numb = list(map(len, otv1))
    if len(Numb) % 2 != 0:
        Numb.append(0)
    i = 0
    kk = []
    while i<len(Numb):
        kk.append(Numb[i] + Numb[i+1])
        i += 2
    print(kk)
    day_lines.append(len(kk))
    all_kk += kk
    #построить график
    
    #подсчет количества ошибок
    last = ''
    numbOfM = 0
    for i in all_actions:
        if i == last:
            numbOfM += 1
        if i == 'П' or i == 'Н':
            last = i
        if i == 'А' or i == 'Б' or i == 'В'or i == 'Г':
            numbOfM += 1
    print('Количество ошибок:', numbOfM)
    
    import matplotlib.pyplot as plt
    plt.title('Length of trial ' + f + "\n" +"Errors total " + str(numbOfM))
    plt.plot(range(len(kk)),kk,'-ro')
    plt.show()
    

plt.title('Length of trial ')
plt.plot(range(len(all_kk)),all_kk,'-ro')
shift = 0
for day in day_lines:
    plt.axvline(x = day+shift)
    shift +=day
plt.show()
print(day_lines)