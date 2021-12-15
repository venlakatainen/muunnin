import math

def kysy_luku_bin_to_dec():
   
    try:
        luku = input("Anna muutettava luku > ")
        print(int(luku, 2))

    except ValueError:
        print("Vaaranlainen syote")

def kysy_luku_dec_to_hex():

    try:
        luku = int(input("Anna muutettava luku >"))
        print(hex(luku))

    except ValueError:
        print("Vaaranlainen syote")

def kysy_luku_dec_to_bin():
    
    try:
        luku = int(input("Anna muutettava luku > "))
        print(bin(luku).replace("0b", ""))

    except ValueError:
        print("Vaaranlainen syote")


def kysy_luku_hex_to_dec():
    
    try:
        luku = str(input("Anna muutettava luku > "))
        print(int(luku, 16))
    
    except ValueError:
        print("Vaaranlainen syote")

def kysy_luku_bin_to_hex():

    try:
        luku = str(input("Anna muutettava luku > "))
        temp = (int(luku, 2))
        print(hex(temp))

    except ValueError:
        print("Vaaranlainen syote")

def kysy_luku_hex_to_bin():

    try:
        luku = str(input("Anna muutettava luku > "))
        luku = (int(luku, 16))
        print(bin(luku).replace("0b", ""))

    except ValueError:
        print("Vaaranlainen syote")


print("1 - binaariluku desimaaliluvuksi")
print("2 - desimaaliluku binaariluvuksi")
print("3 - desimaaliluku heksaluvuksi")
print("4 - heksaluku desimaaliluvuksi")
print("5 - binaariluku heksaluvuksi")
print("6 - heksaluku binaariluvuksi")

try:

    valinta = int(input("Syota valinta > "))


    if (valinta == 1):
        kysy_luku_bin_to_dec()

    elif (valinta == 2):
        kysy_luku_dec_to_bin()

    elif (valinta == 3):
        kysy_luku_dec_to_hex()

    elif (valinta == 4):
        kysy_luku_hex_to_dec()

    elif (valinta == 5):
        kysy_luku_bin_to_hex()

    elif (valinta == 6 ):
        kysy_luku_hex_to_bin()

    else:
        print("Vaaranlainen syote")

except KeyboardInterrupt:
    print("Ohjelma suljetaan.")
