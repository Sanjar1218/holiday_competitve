import pyautogui as pg
import datetime
import time
# 1500 700 (83, 83, 83)
t = 0
count = 0
while True:
    count +=1
    if count%22==0:
        t+=1
    r3,g,b = pg.pixel(428+t,723)
    r4,g,b = pg.pixel(428+t,725)
    r5,g,b = pg.pixel(428+t,728)
    r2,g2,b2 = pg.pixel(430+t, 645)
    if r3<173 or r4<173 or r5<173 or r2<100:
        pg.press('space')
        

