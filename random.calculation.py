import random
import pyautogui as pg
import time 

time.sleep(3)
len = input("How long shoud the numbers be..")
w = ("+","-","*",":","% von ")

for j in range(1):
    for i in range(len):
        pg.write(str(random.randint(0,9)))
    
    pg.write(random.choice(w))

    for i in range(len):
        pg.write(str(random.randint(0,9)))

time.sleep(0.1)
pg.press("enter")
