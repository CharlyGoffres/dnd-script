# MENU 13 TIRADES DE SALVACIO 
# #Pel clear
import os
#Per poder fer que s'esperi el temps
import time


#Per viatjar pels diferents menus
import dice
import menu1
import json
#Per importar les variables
with open("variables.json", "r") as f:
    variables = json.load(f)

#Definició del menu de les tirades de salvació
def fmenu13():
    menu13 = input("Menú de Tirades de Salvació. Aquí tens les opcions: \n(1) Tirada de Salvació de Força \n(2) Tirada de Salvació de Constitució \n(3) Tirada de Salvació de Destresa \n(4) Tirada de Salvació de Sabiduria \n(5) Tirada de Salvació de Inteligència \n(6) Tirada de Salvació de Carisma \n(7) Tira enrere \n(8) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu13:
            case "1":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + ((variables["stats"]["strenght"] - 10) // 2))
                print(dau, ((variables["stats"]["strenght"] - 10) // 2))
                time.sleep(5)
                fmenu13()
            case "2":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de constitució ha estat de: ")
                print(dau + ((variables["stats"]["constitution"] - 10) // 2))
                print(dau, ((variables["stats"]["constitution"] - 10) // 2))
                time.sleep(5)
                fmenu13()
            case "3":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de destresa ha estat de: ")
                print(dau + ((variables["stats"]["dexterity"] - 10) // 2))
                print(dau, ((variables["stats"]["dexterity"] - 10) // 2))
                time.sleep(5)
                fmenu13()
            case "4":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de sabiduria ha estat de: ")
                print(dau + ((variables["stats"]["wisdom"] - 10) // 2) + variables["proficiency"])
                print(dau, ((variables["stats"]["wisdom"] - 10) // 2), variables["proficiency"])
                time.sleep(5)
                fmenu13()
            case "5":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de inteligencia ha estat de: ")
                print(dau + ((variables["stats"]["intelligence"] - 10) // 2) + variables["proficiency"])
                print(dau, ((variables["stats"]["intelligence"] - 10) // 2), variables["proficiency"])
                time.sleep(5)
                fmenu13()
            case "6":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de carisma ha estat de: ")
                print(dau + ((variables["stats"]["charisma"] - 10 // 2)))
                print(dau, ((variables["stats"]["charisma"] - 10 // 2)))
                time.sleep(5)
                fmenu13()
            case "7":
                i = 1
                menu1.fmenu1()
            case "8":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-8 dependent de la opció que vulguis. Torna-ho a provar")
