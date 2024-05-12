print("       hello")
def time(t):
 string=""
 if t//3600000%24<10: string+="0"
 string+=str(t//3600000%24)+":"
 if t//60000%60<10: string+="0"
 string+=str(t//60000%60)+":"
 if t//1000%60<10: string+="0"
 string+=str(t//1000%60)+","
 if t%1000<100: string+="0"
 if t%1000<10: string+="0"
 string+=str(t%1000)
 return string

sub=open("test.srt", "w")
t=0
speed=100
legn=20

txt = "Hello, everyone. My name is Markiplier"+" "*(legn//2)


#main
for i in range(100):
 #number
 string=str(i+1)+"\n"
 #time stamps
 string+=time(t)+" --> "+time(t+speed)+"\n"
 #generate text 
 text=""
 #-------------- 
 for y in range(10):
  if y==0 or y==9: text+="#"+"-"*10+"#"
  else: text+="|"+" "*10+"|"
  text+="\n"
   
# text=("["+"-"*(i%legn)+"#"+"-"*(legn-i%legn-1)+"]"+
#       "\n\n\r["+"-"*(i%legn)+"#"+"-"*(legn-i%legn-1)+"]")

 # --------------		
 string+=text+"\n\n"	
 print(string, end="")
 sub.write(string)
 t+=speed

	
sub.close()
