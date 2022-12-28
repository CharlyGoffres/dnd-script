#MENU 2 DM NO ACABAT
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time

#Per importar les variables
import menu0

#Definció del menu 2 (DM)
#  NO ACABAT
def fmenu2():
    os.system('cls')
    menu2 = input("Benvingut DM. Aquí tens les opcions: \n(1) No sóc el DM, tira enrere \n(2) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu2:
            case "1":
                print("Ops, ara tornes al menú anterior")
                i = 1
                time.sleep(3)
                menu0.fmenu0()
            case "2":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-7 dependent de la opció que vulguis. Torna-ho a provar")
                time.sleep(5)
