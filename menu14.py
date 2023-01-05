#MENU 14 SKILLS
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time

#Per importar les variables

#Per viatjar pels diferents menus
import menu1
import dice
import json
#Per importar les variables
with open("variables.json", "r") as f:
    variables = json.load(f)


#Menu de les de skill
def fmenu14():
    menu14 = input("Menú de Skills. Aquí tens les opcions: \n(1) Acrobatics \n(2) Animal Handling \n(3) Arcana \n(4) Athletics \n(5) Deception \n(6) History \n(7) Insight \n(8) Intimidation \n(9) Investigation \n(10) Medicine \n(11) Nature \n(12) Perception \n(13) Performance \n(14) Persuasion \n(15) Religion \n(16) Sleight of Hand \n(17) Stealth \n(18) Survival \n(19) Tira enrere \n(20) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu14:
            case "1":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Acrobatics ha estat de: ")
                print(dau + ((variables["stats"]["dexterity"] - 10) // 2))
                print(dau, ((variables["stats"]["dexterity"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "2":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Animal Handling ha estat de: ")
                print(dau + ((variables["stats"]["wisdom"] - 10) // 2))
                print(dau, ((variables["stats"]["wisdom"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "3":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Arcana ha estat de: ")
                print(dau + ((variables["stats"]["intelligence"] - 10) // 2) + variables["proficiency"])
                print(dau, ((variables["stats"]["intelligence"] - 10) // 2), variables["proficiency"])
                time.sleep(5)
                fmenu14()
            case "4":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Athletics ha estat de: ")
                print(dau + ((variables["stats"]["strenght"] - 10) // 2))
                print(dau, ((variables["stats"]["strenght"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "5":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Deception ha estat de: ")
                print(dau + ((variables["stats"]["charisma"] - 10 // 2)))
                print(dau, ((variables["stats"]["charisma"] - 10 // 2)))
                time.sleep(5)
                fmenu14()
            case "6":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de History ha estat de: ")
                print(dau + ((variables["stats"]["intelligence"] - 10) // 2) + variables["proficiency"])
                print(dau, ((variables["stats"]["intelligence"] - 10) // 2), variables["proficiency"])
                time.sleep(5)
                fmenu14()
            case "7":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Insight ha estat de: ")
                print(dau + ((variables["stats"]["wisdom"] - 10) // 2))
                print(dau, ((variables["stats"]["wisdom"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "8":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Intimidation ha estat de: ")
                print(dau + ((variables["stats"]["charisma"] - 10 // 2)))
                print(dau, ((variables["stats"]["charisma"] - 10 // 2)))
                time.sleep(5)
                fmenu14()
            case "9":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Investigation ha estat de: ")
                print(dau + ((variables["stats"]["charisma"] - 10 // 2)) + variables["proficiency"])
                print(dau, ((variables["stats"]["charisma"] - 10 // 2)), variables["proficiency"])
                time.sleep(5)
                fmenu14()
            case "10":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Medicine ha estat de: ")
                print(dau + ((variables["stats"]["wisdom"] - 10) // 2))
                print(dau, ((variables["stats"]["wisdom"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "11":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Nature ha estat de: ")
                print(dau + ((variables["stats"]["intelligence"] - 10) // 2))
                print(dau, ((variables["stats"]["intelligence"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "12":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Perception ha estat de: ")
                print(dau + ((variables["stats"]["wisdom"] - 10) // 2))
                print(dau, ((variables["stats"]["wisdom"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "13":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Performance ha estat de: ")
                print(dau + ((variables["stats"]["charisma"] - 10 // 2)))
                print(dau, ((variables["stats"]["charisma"] - 10 // 2)))
                time.sleep(5)
                fmenu14()
            case "14":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Persuasion ha estat de: ")
                print(dau + ((variables["stats"]["charisma"] - 10 // 2)) + variables["proficiency"])
                print(dau, ((variables["stats"]["charisma"] - 10 // 2)), variables["proficiency"])
                time.sleep(5)
                fmenu14()
            case "15":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Religion ha estat de: ")
                print(dau + ((variables["stats"]["intelligence"] - 10) // 2) + variables["proficiency"])
                print(dau, ((variables["stats"]["intelligence"] - 10) // 2), variables["proficiency"])
                time.sleep(5)
                fmenu14()
            case "16":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Sleight of Hand ha estat de: ")
                print(dau + ((variables["stats"]["dexterity"] - 10) // 2))
                print(dau, ((variables["stats"]["dexterity"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "17":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Stealth ha estat de: ")
                print(dau + ((variables["stats"]["dexterity"] - 10) // 2))
                print(dau, ((variables["stats"]["dexterity"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "18":
                i = 1
                dau = dice.fdau(20)
                print("La teva tirada de Survival ha estat de: ")
                print(dau + ((variables["stats"]["wisdom"] - 10) // 2))
                print(dau, ((variables["stats"]["wisdom"] - 10) // 2))
                time.sleep(5)
                fmenu14()
            case "19":
                i = 1
                menu1.fmenu1()
            case "20":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-8 dependent de la opció que vulguis. Torna-ho a provar")