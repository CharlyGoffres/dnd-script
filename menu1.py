#MENU 1 GARGAMELL
# #Pel clear
import os
#Per poder fer que s'esperi el temps
import time

#Per importar les variables
import variables
#Per viatjar pels diferents menus
import menu0
import menu11
import menu12
import menu13
import menu14
import menu15

#Definció del menu 1 (Gargamel), amb les seves 7 opcions
def fmenu1():
    os.system('cls')
    menu1 = input("Benvingut de nou {}. Aquí tens les opcions: \n(1) Vida \n(2) Hechizos \n(3) Tirades de salvació \n(4) Skills \n(5) Rest \n(6) No sóc en Gargamel, tira enrere \n(7) Vull tancar el programa \n".format(variables.Nom_del_personatge))
    i = 0
    while i == 0:
        match menu1:
            case "1":
                print("Has escollit el menú de la Vida")
                i = 1
                time.sleep(3)
                menu11.fmenu11()
            case "2":
                print("Has escollit el menú dels Hechizos")
                i = 1
                time.sleep(3)
                menu12.fmenu12()
            case "3":
                print("Has escollit el menú de les Tirades de Salvació")
                i = 1
                time.sleep(3)
                menu13.fmenu13()
            case "4":
                print("Has escollit el menú dels Skills")
                i = 1
                time.sleep(3)
                menu14.fmenu14()
            case "5":
                print("Has escollit el menú dels Rest")
                i = 1
                time.sleep(3)
                menu15.fmenu15()
            case "6":
                print("Ops, ara tornes al menú anterior")
                i = 1
                time.sleep(3)
                menu0.fmenu0()
            case "7":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-7 dependent de la opció que vulguis. Torna-ho a provar")
                time.sleep(5)