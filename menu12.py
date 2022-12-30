#MENU 12 HECHIZENS
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time

#Per importar les variables
import variables
#Per viatjar pels diferents menus
import menu1


def fmenu12():
    os.system('cls')
    menu12 = input("Menú dels hechizos. Aquí tens les opcions: \n(1) Veure el nombre de Spell Slots \n(2) Llista de Spells \n(3) Atacar \n(4) Tira enrere \n(5) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu12:
            case "1":
                i = 1
                print("Tens:\nHechizens de Nivell 1: {}/{}\nHechizens de Nivell 2: {}/{}\nHechizens de Nivell 3: {}/{}\nHechizens de Nivell 4: {}/{}".format(variables.Spell_Level_1, variables.Spell_Level_1_Max, variables.Spell_Level_2, variables.Spell_Level_2_Max, variables.Spell_Level_3, variables.Spell_Level_3_Max, variables.Spell_Level_4, variables.Spell_Level_4_Max))
                time.sleep(3)
                fmenu12()
            case "2":
                i = 1
                fmenu122()
            case "3":
                i = 1
                fmenu123()
            case "4":
                i = 1
                fmenu1()
            case "5":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-5 dependent de la opció que vulguis. Torna-ho a provar")