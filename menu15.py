#MENU 15 REST NO ACABAT
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time

#Per importar les variables

#Per viatjar pels diferents menus
import dice
import menu1
import json
#Per importar les variables
with open("variables.json", "r") as f:
    variables = json.load(f)

#Menu de les Rest 
# NO ACABAT
def fmenu15():
    menu15 = input("Menú de Rests. Aquí tens les opcions: \n(1) Long Rest \n(2) Short Rest \n(3) Tira enrere \n(4) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu15:
            case "1":
                i = 1
                #Long rest
                dau = dice.fdau(20)
                print("La teva tirada de Acrobatics ha estat de: ")
                print(dau + variables.Modificador_Dexterity)
                print(dau, variables.Modificador_Dexterity)
                time.sleep(5)
                fmenu15()
            case "2":
                i = 1
                #Short rest
                dau = dice.fdau(20)
                print("La teva tirada de Animal Handling ha estat de: ")
                print(dau + variables.Modificador_Wisdom)
                print(dau, variables.Modificador_Wisdom)
                time.sleep(5)
                fmenu15()
            case "3":
                i = 1
                menu1.fmenu1()
            case "4":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-8 dependent de la opció que vulguis. Torna-ho a provar")
