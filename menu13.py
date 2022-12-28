# #Pel clear
import os
#Per poder fer que s'esperi el temps
import time

#Per importar les variables
import variables
#Per viatjar pels diferents menus
import dice
import menu1


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
                print(dau + variables.Modificador_Strengh)
                print(dau, variables.Modificador_Strengh)
                time.sleep(5)
                fmenu13()
            case "2":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + variables.Modificador_Constitution)
                print(dau, variables.Modificador_Constitution)
                time.sleep(5)
                fmenu13()
            case "3":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + variables.Modificador_Dexterity)
                print(dau, variables.Modificador_Dexterity)
                time.sleep(5)
                fmenu13()
            case "4":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + variables.Modificador_Wisdom + variables.Proficiency_Bonus)
                print(dau, variables.Modificador_Wisdom, variables.Proficiency_Bonus)
                time.sleep(5)
                fmenu13()
            case "5":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + variables.Modificador_Intelligence + variables.Proficiency_Bonus)
                print(dau, variables.Modificador_Intelligence, variables.Proficiency_Bonus)
                time.sleep(5)
                fmenu13()
            case "6":
                dau = dice.fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + variables.Modificador_Charisma)
                print(dau, variables.Modificador_Charisma)
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
