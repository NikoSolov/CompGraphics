import pandas as pd
from os import listdir

folderIn = "FFT_delta/"
folderOut= "FFT_delta_excel/"
files=listdir(folderIn)

if False:
 fl=False
 for filename in files:
  f=open(folderIn+filename, 'r')
  txt=""
  for line in f:
   print("[",line,"]")
   if line!="\n":
    for sym in line:
     if sym==" ": fl=True
     else:
       if fl==True:
        txt+="\t"
  #      print(txt)
       fl=False
       txt+=sym 
 #   txt+="\n"
 #   print("newline")
  f.close()
  fout=open(folderIn+filename, 'w')
  fout.write(txt)
  fout.close()
 #print(txt)
else:
 df2=[]
# fil2=[pd.DataFrame({"File":})]
 df3=[]
 for filename in files:
  fin=open(folderIn+filename, 'r')
  print(filename)
  df = pd.read_csv(folderIn+filename, sep='\t')
  del df[df.columns[-1]]
  #--------------------------------
  lib={"delta1":"0.5-2","delta2":"2-4", "delta.":"0.5-4"}
  
  for i in lib.keys():
   if i in filename:
    head=list(df.columns)
    for j in range(1,len(head)):
     if "2_" in filename:
       head[j]+="_M_"+lib[i]
     else:
       head[j]+="_T_"+lib[i]
    df.columns=head
  #-------------------------------
#  indx=-1
#  filen=list(df["File"])
#  for i in range(len(filen)):
#   if "KUDRYASHOVA" in filen[i]:
#    indx=filen[i]
#  print(filen[i])
#  if indx!=-1:
#   df.T.pop(indx)

#   df.append(df.pop(indx))
   
#  df.index[df['column_name']==value].tolist()
#-------------------------------------------
  if "wake2" in filename or "wakeb2" in filename or "wakewake2" in filename:
   df2.append(df.iloc[:,1:])
  else:
   df3.append(df.iloc[:,1:])

#-------------------------------------------
  df.to_excel(folderOut+filename[:-4]+".xlsx", '1')
  print("DONE!!!")
  fin.close()

#-------------------------------
  result2 = pd.concat(df2, axis=1)
#print(len(["ANOHINA_2","BESKROVNAYA_1","DETKOVA_1","DUBAR_1","FATUEVA_2","GALKIN_1","GRINEVA_1","IVANOVA_1","KADIROV_2","KOKURKINA_2","KOROVINA_2","LADIK_1","MAMEDOVA_1","MATCUKEVIH_2","PEREGUDOVA_2","PLOTNIKOVA_2","ROTARU_1","SAZIN_1","SHAPKINA_3","SHEVALDOVA_2","SIBIRYAKINA_1","SIDORENKO_2","SOLOVEVA_1","SURKOV_1","TSIBA_2","VIRYASOVA_2"]))

 result2.insert(0, "File", ["ANOHINA_2","BESKROVNAYA_1","DETKOVA_1","DUBAR_1","FATUEVA_2","GALKIN_1","GRINEVA_1","IVANOVA_1","KADIROV_2","KOKURKINA_2","KOROVINA_2","LADIK_1","MAMEDOVA_1","MATCUKEVIH_2","PEREGUDOVA_2","PLOTNIKOVA_2","ROTARU_1","SAZIN_1","SHAPKINA_3","SHEVALDOVA_2","SIBIRYAKINA_1","SIDORENKO_2","SOLOVEVA_1","SURKOV_1","TSIBA_2","VIRYASOVA_2"], True)
 result3 = pd.concat(df3, axis=1)
 result3.insert(0, "File", [
"ANOHINA_1",
"BESKROVNAYA_2",
"DETKOVA_2",
"DUBAR_2",
"FATUEVA_1",
"GALKIN_2",
"GRINEVA_3",
"IVANOVA_2",
"KADIROV_1",
"KOKURKINA_1",
"KOROVINA_1",
"KUDRYASHOVA_1",
"LADIK_2",
"MAMEDOVA_2",
"MATCUKEVIH_1",
"PEREGUDOVA_1",
"PLOTNIKOVA_1",
"ROTARU_2",
"SAZIN_03",
"SHAPKINA_1",
"SHEVALDOVA_1",
"SIBIRYAKINA_2",
"SIDORENKO_1",
"SOLOVEVA_2",
"SURKOV_2",
"TSIBA_1",
])
 result2.to_excel(folderOut+"wake2"+".xlsx", '1')
 result3.to_excel(folderOut+"wake3"+".xlsx", '1')
