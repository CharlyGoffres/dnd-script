#MENU 11 DE LA VIDA
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time


#Per viatjar pels diferents menus
import menu1
import json
#Per importar les variables
with open("variables.json", "r") as f:
    variables = json.load(f)

#Definició del menu de la vida
def fmenu11():
    os.system('cls')
#Aqui ja demana les opcions del menú
    menu11 = input("Menú de la Vida. Aquí tens les opcions: \n(1) Veure la Vida \n(2) Treure Vida \n(3) Curar Vida \n(4) Canviar la vida que tinc manualment \n(5) Tira enrere \n(6) Vull tancar el programa \n")
    i = 0
    while i == 0:
        match menu11:
            case "1":
                i = 1
                print("La teva vida és : {}/{}".format(variables["vida"]["vida"], variables["vida"]["vida_max"]))
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
                variables["vida"]["vida"] = int(input("Hola, has entrat al menú de la Vida però no sé quanta vida tens. Pots introduir la quantitat de vida que tens. \nRecorda que el teu màxim és: {} \n".format(variables["vida"]["vida_max"])))
                print ("La teva vida ara és de {}/{}".format(variables["vida"]["vida"], variables["vida"]["vida_max"]))
                with open("variables.json", "w") as f:
                    json.dump(variables, f)
                time.sleep(5)
                fmenu11()
            case "5":
                i = 1
                menu1.fmenu1()
            case "6":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-5 dependent de la opció que vulguis. Torna-ho a provar")
                i = 1
                time.sleep(2)
                fmenu11()


#Definim la funció de treure vida
def fmenu112():
    while True:
            try:
                # Comprovem que el input que han introduit sigui un nombre, amb la funció int, sino es un numero saltarà l'error
                Damage = int(input("Escriu quanta vida t'han tret \n"))
                variables["vida"]["vida"]
                variables["vida"]["vida"] -= Damage
                break
            except ValueError:
                print("Vaja, no t'he entés. Recorda que has de posar un número amb la quantitat de vida que t'han tret. Torna-ho a provar")
    print("La teva vida ara és de {}/{}".format(variables["vida"]["vida"], variables["vida"]["vida_max"]))
    with open("variables.json", "w") as f:
        json.dump(variables, f)
    time.sleep(5)
    fmenu11()


#Definim la funció de curar vida
def fmenu113():
    while True:
            try:
                # Comprovem que el input que han introduit sigui un nombre, amb la funció int, sino es un numero saltarà l'error
                Cura = int(input("Escriu quanta vida t'has curat \n"))
                variables["vida"]["vida"] += Cura
                if variables["vida"]["vida"] > variables["vida"]["vida_max"]:
                    variables["vida"]["vida"] = variables["vida"]["vida_max"]
                break
            except ValueError:
                print("Vaja, no t'he entés. Recorda que has de posar un número amb la quantitat de vida que t'han tret. Torna-ho a provar")
    print("La teva vida ara és de {}/{}".format(variables["vida"]["vida"], variables["vida"]["vida_max"]))
    with open("variables.json", "w") as f:
        json.dump(variables, f)
    time.sleep(5)
    fmenu11()
