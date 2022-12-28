#MENU 0
# #Pel clear
import os
#Per poder fer que s'esperi el temps
import time
#Per poder fer el random dels daus
import random

#Per importar les variables
import variables
import menu1
import menu2

#Funció del primer menú amb les 3 opcions
def fmenu0():
    os.system('cls')
    menu0 = input("(1) Entres com a {} \n(2) Entres com a DM \n(3) Vull tancar el programa \n".format(variables.Nom_del_personatge))
    i = 0
    while i == 0:
        match menu0:
            case "1":
                print("Si has pujat de nivell, recorda actualitzar el codi")
                i = 1
                time.sleep(3)
                menu1.fmenu1()
            case "2":
                print("Has entrat a la opció 2")
                i = 1
                time.sleep(2)
                menu2.fmenu2()
            case "3":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-3 dependent de la opció que vulguis. Torna-ho a provar")
                time.sleep(5)