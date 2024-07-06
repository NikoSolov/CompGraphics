from os import get_terminal_size, system

width, height=get_terminal_size()
prnt=lambda text: print(text, end="", flush=True)
coord=lambda x,y: prnt(f"\033[{y};{x}H")
clear=lambda: system("clear")
color=lambda c: print(f"\033[{c}m")
def cursor_hide(bl):
 if bl: prnt("\033[?25l")
 else:  prnt("\033[?25h")

prnt("\a") 
