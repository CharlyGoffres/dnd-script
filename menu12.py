#MENU 12 HECHIZENS
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time

import menu1
import json
#Per importar les variables
with open("variables.json", "r") as f:
    variables = json.load(f)
#Per viatjar pels diferents menus



def fmenu12():
    os.system('cls')
    menu12 = input("Menú dels hechizos. Aquí tens les opcions: \n(1) Veure el nombre de Spell Slots \n(2) Llista de Spells \n(3) Atacar \n(4) Canviar manualment el nombre de spell slots \n(5) Tira enrere \n(6) Vull tancar el programa \n")
       
    i = 0
    while i == 0:
        match menu12:
            case "1":
                i = 1
                print("Tens:\nHechizens de Nivell 1: {}/{}\nHechizens de Nivell 2: {}/{}\nHechizens de Nivell 3: {}/{}\nHechizens de Nivell 4: {}/{}".format(variables["spell_slots"]["spell_level_1"], variables["spell_slots"]["spell_level_1_max"], variables["spell_slots"]["spell_level_2"], variables["spell_slots"]["spell_level_2_max"], variables["spell_slots"]["spell_level_3"], variables["spell_slots"]["spell_level_3_max"], variables["spell_slots"]["spell_level_4"], variables["spell_slots"]["spell_level_4_max"]))
                time.sleep(3)
                fmenu12()
            case "2":
                # Obtiene la lista de hechizos
                spells = variables["hechizos"]
                # Agrupa los hechizos según su nivel
                spells_by_level = {}
                for spell in spells:
                    level = spell["level"]
                    if level not in spells_by_level:
                        spells_by_level[level] = []
                    spells_by_level[level].append(spell)
                # Imprime un menú con las secciones correspondientes a cada nivel de hechizo
                print("Aquí tens els teus hechizos:")
                for level, level_spells in spells_by_level.items():
                    print(f"Nivel {level}:")
                    for i, spell in enumerate(level_spells):
                        print(f"  {i+1}. {spell['nombre']}")
                print()
                i = 1
                fmenu12()
            case "3":
                i = 1
                fmenu123()
            case "4":
                i = 1
                fmenu124()
            case "5":
                i = 1
                fmenu1()
            case "6":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-6 dependent de la opció que vulguis. Torna-ho a provar")

