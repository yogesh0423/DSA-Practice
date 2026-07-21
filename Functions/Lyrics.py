import time
import sys

def print_lyrics():

    lyrics = [

    "Mein ab kyun hosh mai aata nahi?",
    "Sukoon yeh dil kyun paata nahi?",
    "Kyun todun khud se jo the waade",
    "Ke ab yeh ishq nibhaana nahi?",
    "Mein modun tum se jo yeh chehra",
    "Dobara nazar milana nahi",
    "Yeh duniya jaane mera dard",
    "Tujhe yeh nazar kyun aata nahi?"

    ]

    delays = [ 0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8, ]

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print(" Pal Pal : \n")

time.sleep(1.2)

print_lyrics()