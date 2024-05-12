# ------- functions -----
def wire(file, fr, to):
 f.write(" "*space+'<wire from="('+str(fr[0]*10)+','+str(fr[1]*10)+')" to="('+str(to[0]*10)+','+str(to[1]*10)+')"/>\n')

def clock(file, pos, direct):
 f.write(" "*space+'<comp lib="0" loc="('+str(pos[0]*10)+','+str(pos[1]*10)+')" name="Clock">\n'+" "*(space+2)+
       '<a name="facing" val="'+direct+'"/>\n'+" "*space+'</comp>\n')
def flop(file, pos):
 f.write(" "*space+'<comp lib="4" loc="('+str((pos[0]+4)*10)+','+str(pos[1]*10)+')" name="D Flip-Flop">\n'+
      " "*(space+2)+'<a name="appearance" val="classic"/>\n'+" "*space+'</comp>\n')
# -----------------------
f=open("test.circ","w")
fexmp=open("exmp.txt","r")
f.write(fexmp.read())
fexmp.close()
space=4
# ----- write yours ----
clock(f, (4,4), "east")
wire(f, (4,4), (5,4))
wire(f, (5,4), (5,8))
wire(f, (5,8), (10,8))
flop(f, (10,8))


# ----------------------
f.write("  </circuit>\n</project>")
f.close()
