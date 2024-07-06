import pyautogui as pg
from time import sleep


#pg.write('Hello,', interval=0.25)
pg.hotkey('winleft', 's')
pg.write('note')
pg.press('enter')
sleep(1)
pg.write('hello')

pg.hotkey('ctrl', 's')
sleep(1)
pg.write('test.txt')
pg.press('enter')
