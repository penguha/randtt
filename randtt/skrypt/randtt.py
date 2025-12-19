import random
import time

print("randtt made by : penguha")
time.sleep(3)

imie = input('wprowadź swój nick, imie lub co chcesz: ')

slowa = ["sraczka", "niewiem", "pizdzik", "zbyt", "kurtak", "67uameri", "jestem", "gryzon", "debyl", "kupka"]
liczby = random.randint(100, 1001)

print("twoj nick to : " + random.choice(slowa) + imie + str(liczby))