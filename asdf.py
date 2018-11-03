from pynput.keyboard import Key, Controller
import nltk

import time

keyboard=Controller()
a=str(input("type"))
print(a.split())

time.sleep(3)

for i in a:
    keyboard.type(i)

    time.sleep(0.03)





