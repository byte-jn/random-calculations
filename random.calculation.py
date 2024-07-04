import random
import time 

len = int(input("How long shoud the numbers be.. "))
w = ("+","-","*",":","% von ")
x = ""
z = ""

for j in range(1):
    for i in range(len):
        x = x + (str(random.randint(0,9)))
    
    y = (random.choice(w))

    for i in range(len):
        z = z +(str(random.randint(0,9)))

print(str(x)+ " " + y + " " + str(z))
time.sleep(10)
