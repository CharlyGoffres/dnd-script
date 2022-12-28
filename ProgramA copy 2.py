#Importem packages
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time
#Per poder fer el random dels daus
import random


#Informació sobre el personatge
Level = 7
Hit_dice = 6
Modificador_Strengh_pur = 8
Modificador_Strengh = (Modificador_Strengh_pur - 10) // 2
Modificador_Constitution_pur = 14
Modificador_Constitution = (Modificador_Constitution_pur - 10) // 2
Modificador_Dexterity_pur = 14
Modificador_Dexterity = (Modificador_Dexterity_pur - 10) // 2
Modificador_Wisdom_pur = 18
Modificador_Wisdom = (Modificador_Wisdom_pur - 10) // 2
Modificador_Intelligence_pur = 12
Modificador_Intelligence = (Modificador_Intelligence_pur - 10) // 2
Modificador_Charisma_pur = 10
Modificador_Charisma = (Modificador_Charisma_pur - 10) // 2
Armor_Class = 17
Initiative = 2
Proficiency_Bonus = 3
Vida_max = 44
Vida = 10011999
Spell_Level_1 = 4
Spell_Level_2 = 3
Spell_Level_3 = 3
Spell_Level_4 = 1
Spell_Level_1_Max = 4
Spell_Level_2_Max = 3
Spell_Level_3_Max = 3
Spell_Level_4_Max = 1


# Genera un número aleatori entre 1 i el número de caras del dau
def fdau(cares):
    resultat = random.randint(1, cares)
    return resultat


#Iniciem el programa, iniciant la funció finici
def finici():
    print ("Benvigunt al programa d'Automatització de vida i dany d'en Goffres")
    time.sleep(3)
    fmenu0()   


#Funció del primer menú amb les 3 opcions
def fmenu0():
    os.system('cls')
    menu0 = input("(1) Entres com a Gargamel \n(2) Entres com a DM \n(3) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu0:
            case "1":
                print("Si has pujat de nivell, recorda actualitzar el codi")
                i = 1
                time.sleep(3)
                fmenu1()
            case "2":
                print("Has entrat a la opció 2")
                i = 1
                time.sleep(2)
                fmenu2()
            case "3":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-3 dependent de la opció que vulguis. Torna-ho a provar")
                time.sleep(5)



    



#Definció del menu 1 (Gargamel), amb les seves 7 opcions
def fmenu1():
    os.system('cls')
    menu1 = input("Benvingut de nou Gargamel. Aquí tens les opcions: \n(1) Vida \n(2) Hechizos \n(3) Tirades de salvació \n(4) Skills \n(5) Rest \n(6) No sóc en Gargamel, tira enrere \n(7) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu1:
            case "1":
                print("Has escollit el menú de la Vida")
                i = 1
                time.sleep(3)
                fmenu11()
            case "2":
                print("Has escollit el menú dels Hechizos")
                i = 1
                time.sleep(3)
                fmenu12()
            case "3":
                print("Has escollit el menú de les Tirades de Salvació")
                i = 1
                time.sleep(3)
                fmenu13()
            case "4":
                print("Has escollit el menú dels Skills")
                i = 1
                time.sleep(3)
                fmenu14()
            case "5":
                print("Has escollit el menú dels Rest")
                i = 1
                time.sleep(3)
                fmenu15()
            case "6":
                print("Ops, ara tornes al menú anterior")
                i = 1
                time.sleep(3)
                fmenu0()
            case "7":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-7 dependent de la opció que vulguis. Torna-ho a provar")
                time.sleep(5)


#Definició del menu de la vida
def fmenu11():
    os.system('cls')
    # verificar si se quanta vida té
    global Vida
    if Vida == 10011999:
        # Si no he introduit una vegada la quantitat de vida que tinc, hauré d'introduir-lo
        while True:
            try:
                # Comprovem que el input que han introduit sigui un nombre, amb la funció int, sino es un numero saltarà l'error
                Vida = int(input("Hola, has entrat al menú de la Vida però no sé quanta vida tens. Pots introduir la quantitat de vida que tens. \nRecorda que el teu màxim és: {} \n".format(Vida_max)))
                break
            except ValueError:
                print("Vaja, no t'he entés. Recorda que has de posar un número amb la teva quantitat de vida. Torna-ho a provar")
    else:
         # Si la variable Vida està actualitzada, surtirà aquest missatge.
        print("M'enrecordo de la teva vida")
#Aqui ja demana les opcions del menú
    menu11 = input("Menú de la Vida. Aquí tens les opcions: \n(1) Veure la Vida \n(2) Treure Vida \n(3) Curar Vida \n(4) Canviar la vida que tinc manualment \n(5) Tira enrere \n(6) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu11:
            case "1":
                i = 1
                print("La teva vida és : {}/{}".format(Vida, Vida_max))
                time.sleep(5)
                fmenu11()
            case "2":
                i = 1
                fmenu112()
            case "3":
                i = 1
                fmenu113()
            case "4":
                i = 1
                Vida = int(input("Hola, has entrat al menú de la Vida però no sé quanta vida tens. Pots introduir la quantitat de vida que tens. \nRecorda que el teu màxim és: {} \n".format(Vida_max)))
                print ("La teva vida ara és de {}/{}".format(Vida, Vida_max))
                time.sleep(5)
                fmenu11()
            case "5":
                i = 1
                fmenu1()
            case "6":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-5 dependent de la opció que vulguis. Torna-ho a provar")
                fmenu1()

#Definim la funció de treure vida
def fmenu112():
    while True:
            try:
                # Comprovem que el input que han introduit sigui un nombre, amb la funció int, sino es un numero saltarà l'error
                Damage = int(input("Escriu quanta vida t'han tret \n"))
                global Vida
                Vida -= Damage
                break
            except ValueError:
                print("Vaja, no t'he entés. Recorda que has de posar un número amb la quantitat de vida que t'han tret. Torna-ho a provar")
    print("La teva vida ara és de {}/{}".format(Vida, Vida_max))
    time.sleep(5)
    fmenu11()

#Definim la funció de curar vida
def fmenu113():
    while True:
            try:
                # Comprovem que el input que han introduit sigui un nombre, amb la funció int, sino es un numero saltarà l'error
                Cura = int(input("Escriu quanta vida t'has curat \n"))
                global Vida
                Vida += Cura
                if Vida > Vida_max:
                    Vida = Vida_max
                break
            except ValueError:
                print("Vaja, no t'he entés. Recorda que has de posar un número amb la quantitat de vida que t'han tret. Torna-ho a provar")
    print("La teva vida ara és de {}/{}".format(Vida, Vida_max))
    time.sleep(5)
    fmenu11()


#Definició del menu dels hechizos 
# NO ACABAT
def fmenu12():
    os.system('cls')
    menu12 = input("Menú dels hechizos. Aquí tens les opcions: \n(1) Veure el nombre de Spell Slots \n(2) Llista de Spells \n(3) Atacar \n(4) Tira enrere \n(5) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu12:
            case "1":
                i = 1
                print("Tens:\nHechizens de Nivell 1: {}/{}\nHechizens de Nivell 2: {}/{}\nHechizens de Nivell 3: {}/{}\nHechizens de Nivell 4: {}/{}".format(Spell_Level_1, Spell_Level_1_Max, Spell_Level_2, Spell_Level_2_Max, Spell_Level_3, Spell_Level_3_Max, Spell_Level_4, Spell_Level_4_Max))
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


#Definició del menu de les tirades de salvació
def fmenu13():
    menu13 = input("Menú de Tirades de Salvació. Aquí tens les opcions: \n(1) Tirada de Salvació de Força \n(2) Tirada de Salvació de Constitució \n(3) Tirada de Salvació de Destresa \n(4) Tirada de Salvació de Sabiduria \n(5) Tirada de Salvació de Inteligència \n(6) Tirada de Salvació de Carisma \n(7) Tira enrere \n(8) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu13:
            case "1":
                dau = fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + Modificador_Strengh)
                print(dau, Modificador_Strengh)
                time.sleep(5)
                fmenu13()
            case "2":
                dau = fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + Modificador_Constitution)
                print(dau, Modificador_Constitution)
                time.sleep(5)
                fmenu13()
            case "3":
                dau = fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + Modificador_Dexterity)
                print(dau, Modificador_Dexterity)
                time.sleep(5)
                fmenu13()
            case "4":
                dau = fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + Modificador_Wisdom + Proficiency_Bonus)
                print(dau, Modificador_Wisdom, Proficiency_Bonus)
                time.sleep(5)
                fmenu13()
            case "5":
                dau = fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + Modificador_Intelligence + Proficiency_Bonus)
                print(dau, Modificador_Intelligence, Proficiency_Bonus)
                time.sleep(5)
                fmenu13()
            case "6":
                dau = fdau(20)
                i = 1
                print("La teva tirada de salvació de força ha estat de: ")
                print(dau + Modificador_Charisma)
                print(dau, Modificador_Charisma)
                time.sleep(5)
                fmenu13()
            case "7":
                i = 1
                fmenu1()
            case "8":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-8 dependent de la opció que vulguis. Torna-ho a provar")


#Menu de les de skill
def fmenu14():
    menu14 = input("Menú de Skills. Aquí tens les opcions: \n(1) Acrobatics \n(2) Animal Handling \n(3) Arcana \n(4) Athletics \n(5) Deception \n(6) History \n(7) Insight \n(8) Intimidation \n(9) Investigation \n(10) Medicine \n(11) Nature \n(12) Perception \n(13) Performance \n(14) Persuasion \n(15) Religion \n(16) Sleight of Hand \n(17) Stealth \n(18) Survival \n(19) Tira enrere \n(20) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu14:
            case "1":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Acrobatics ha estat de: ")
                print(dau + Modificador_Dexterity)
                print(dau, Modificador_Dexterity)
                time.sleep(5)
                fmenu14()
            case "2":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Animal Handling ha estat de: ")
                print(dau + Modificador_Wisdom)
                print(dau, Modificador_Wisdom)
                time.sleep(5)
                fmenu14()
            case "3":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Arcana ha estat de: ")
                print(dau + Modificador_Intelligence + Proficiency_Bonus)
                print(dau, Modificador_Intelligence, Proficiency_Bonus)
                time.sleep(5)
                fmenu14()
            case "4":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Athletics ha estat de: ")
                print(dau + Modificador_Strengh)
                print(dau, Modificador_Strengh)
                time.sleep(5)
                fmenu14()
            case "5":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Deception ha estat de: ")
                print(dau + Modificador_Charisma)
                print(dau, Modificador_Charisma)
                time.sleep(5)
                fmenu14()
            case "6":
                i = 1
                dau = fdau(20)
                print("La teva tirada de History ha estat de: ")
                print(dau + Modificador_Intelligence + Proficiency_Bonus)
                print(dau, Modificador_Intelligence, Proficiency_Bonus)
                time.sleep(5)
                fmenu14()
            case "7":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Insight ha estat de: ")
                print(dau + Modificador_Wisdom)
                print(dau, Modificador_Wisdom)
                time.sleep(5)
                fmenu14()
            case "8":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Intimidation ha estat de: ")
                print(dau + Modificador_Charisma)
                print(dau, Modificador_Charisma)
                time.sleep(5)
                fmenu14()
            case "9":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Investigation ha estat de: ")
                print(dau + Modificador_Charisma + Proficiency_Bonus)
                print(dau, Modificador_Charisma, Proficiency_Bonus)
                time.sleep(5)
                fmenu14()
            case "10":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Medicine ha estat de: ")
                print(dau + Modificador_Wisdom)
                print(dau, Modificador_Wisdom)
                time.sleep(5)
                fmenu14()
            case "11":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Nature ha estat de: ")
                print(dau + Modificador_Intelligence)
                print(dau, Modificador_Intelligence)
                time.sleep(5)
                fmenu14()
            case "12":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Perception ha estat de: ")
                print(dau + Modificador_Wisdom)
                print(dau, Modificador_Wisdom)
                time.sleep(5)
                fmenu14()
            case "13":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Performance ha estat de: ")
                print(dau + Modificador_Charisma)
                print(dau, Modificador_Charisma)
                time.sleep(5)
                fmenu14()
            case "14":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Persuasion ha estat de: ")
                print(dau + Modificador_Charisma + Proficiency_Bonus)
                print(dau, Modificador_Charisma, Proficiency_Bonus)
                time.sleep(5)
                fmenu14()
            case "15":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Religion ha estat de: ")
                print(dau + Modificador_Intelligence + Proficiency_Bonus)
                print(dau, Modificador_Intelligence, Proficiency_Bonus)
                time.sleep(5)
                fmenu14()
            case "16":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Sleight of Hand ha estat de: ")
                print(dau + Modificador_Dexterity)
                print(dau, Modificador_Dexterity)
                time.sleep(5)
                fmenu14()
            case "17":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Stealth ha estat de: ")
                print(dau + Modificador_Dexterity)
                print(dau, Modificador_Dexterity)
                time.sleep(5)
                fmenu14()
            case "18":
                i = 1
                dau = fdau(20)
                print("La teva tirada de Survival ha estat de: ")
                print(dau + Modificador_Wisdom)
                print(dau, Modificador_Wisdom)
                time.sleep(5)
                fmenu14()
            case "19":
                i = 1
                fmenu1()
            case "20":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-8 dependent de la opció que vulguis. Torna-ho a provar")

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
                dau = fdau(20)
                print("La teva tirada de Acrobatics ha estat de: ")
                print(dau + Modificador_Dexterity)
                print(dau, Modificador_Dexterity)
                time.sleep(5)
                fmenu14()
            case "2":
                i = 1
                #Short rest
                dau = fdau(20)
                print("La teva tirada de Animal Handling ha estat de: ")
                print(dau + Modificador_Wisdom)
                print(dau, Modificador_Wisdom)
                time.sleep(5)
                fmenu14()
            case "3":
                i = 1
                fmenu1()
            case "4":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-8 dependent de la opció que vulguis. Torna-ho a provar")




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
                fmenu0()
            case "2":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-7 dependent de la opció que vulguis. Torna-ho a provar")
                time.sleep(5)




#Per començar el programa s'ha de escriure la funció                
finici()