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

sub=open("Test.srt", "w")
t=0
speed=100
txt = "Hello, everyone. My name is Markiplier"


#main
for i in range(1000):
	#number
	string=str(i+1)+"\n"
	#time stamps
	string+=time(t)+" --> "+time(t+speed)+"\n"
	#generate text 
	text=""
#--------------
    
#--------------		
	string+="\n\n"	
	sub.write(string)
	t+=speed
	
	
sub.close()