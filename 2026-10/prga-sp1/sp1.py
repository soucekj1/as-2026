#20
#12.10.2026
#Kulička s tabulkou
import time
import math


pocet = int(input("Kolik má být kuliček? "))


for i in range(pocet):
    print(f"Kulička {i+1} jede!")

    # Animace
for i in range(pocet):
    print(" " * i + "O")
    time.sleep(0.1)  # Pauza mezi snímky animace

    # Animace pro kuličku zpět
for i in range(pocet - 2, 0, -1):
    print(" " * i + "O")
    time.sleep(0.1)  # Pauza mezi snímky animace

time.sleep(0.5)  # Pauza po dokončení animace
print("Tabulka")
for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))