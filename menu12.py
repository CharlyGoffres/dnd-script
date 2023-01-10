#MENU 12 HECHIZENS
#Pel clear
import os
#Per poder fer que s'esperi el temps
import time
import re
import dice
import menu12
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
                #MENU PER SABER ELS SPELLS SLOTS
                i = 1
                print("Tens:\nHechizens de Nivell 1: {}/{}\nHechizens de Nivell 2: {}/{}\nHechizens de Nivell 3: {}/{}\nHechizens de Nivell 4: {}/{}".format(variables["spell_slots"]["spell_level_1"], variables["spell_slots"]["spell_level_1_max"], variables["spell_slots"]["spell_level_2"], variables["spell_slots"]["spell_level_2_max"], variables["spell_slots"]["spell_level_3"], variables["spell_slots"]["spell_level_3_max"], variables["spell_slots"]["spell_level_4"], variables["spell_slots"]["spell_level_4_max"]))
                time.sleep(3)
                fmenu12()
            case "2":
                #MENU PER SABER ELS HECHIZOS
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
                time.sleep(3)
                fmenu12()
            case "3":
                i = 1
                fmenu123()
            case "4":
                i = 1
                fmenu124()
            case "5":
                i = 1
                menu1.fmenu1()
            case "6":
                os.system('cls')
                print("Txao txao!")
                i = 1
            case _:
                print("Vaja, no t'he entés. Recorda que has de posar un número del 1-6 dependent de la opció que vulguis. Torna-ho a provar")


#MENU 123 ATAC DELS HECHIZOS

def fmenu123():
    # Obtiene la lista de hechizos
    spells = variables["hechizos"]

    # Imprime un menú con los nombres de los hechizos
    print("Selecciona un hechizo:")
    print()
    for i, spell in enumerate(spells):
        print(f"{i+1}. {spell['nombre']} (Nivel {spell['level']})")

    # Pide al usuario que elija un hechizo
    choice = int(input())

    # Muestra la información del hechizo elegido
    selected_spell = spells[choice - 1]

    # Pide al usuario que ingrese el nivel del hechizo

    e = 0
    while e == 0:
    # Pide al usuario que ingrese el nivel del hechizo
        level = int(input(f"Ingresa el nivel de {selected_spell['nombre']}, el nivel base del hechizo es {selected_spell['level']}: "))
        # Verifica si el nivel ingresado es correcto
        if level >= selected_spell['level']:
            e = 1
            k = 0
            while k == 0:
        # Pide al usuario si quiere lanzar el hechizo
                answer = input(f"¿Quieres lanzar este {selected_spell['nombre']} de nivel {level} ? (S/N) ")

        # Si el usuario quiere lanzar el hechizo, muestra la información de nuevo
                if answer.lower() == "s":
                    print(f"Lanzando hechizo: {selected_spell['nombre']}")
                    k = 1
                    use_spell(selected_spell['nombre'],level)
            
        # Si el usuario no quiere lanzar el hechizo, ejecuta la función fmenu124()
                elif answer.lower() == "n":
                    k = 1
                else:
                    print("Perdona no t'he entés.")
        else:
            e = 0
            print(f"Tienes que introducir un valor superior o igual a {selected_spell['level']}")

    with open("variables.json", "w") as f:
        json.dump(variables, f)
    fmenu123()




def lanzar_dados(damage_dice):
    # Extraemos los números de la cadena
    resultado = re.findall(r'\d+', damage_dice)
    
    # Si no se encontraron dos números, devolvemos None
    if resultado is None:
        return None
    
    # Desempaquetamos la tupla
    veces, valor = resultado
    
    # Lanzamos los dados "veces" veces y guardamos los resultados en una lista
    return [(dice.fdau(int(valor))) for _ in range(int(veces))]


def use_spell(spell_name, spell_level):
    if spell_level != 0:
    # Get the maximum and remaining number of spells for the given level
        spell_level_max = variables['spell_slots'][f'spell_level_{spell_level}_max']
        spell_level_remaining = variables['spell_slots'][f'spell_level_{spell_level}']

        # Return None if there are no remaining spells
        if spell_level_remaining == 0:
            print("No tienes mas hechizos de este nivel")
            fmenu123()
        else:
            # Decrement the number of remaining spells by 1
            spell_level_remaining -= 1

        # Update the number of remaining spells in the JSON data
        variables['spell_slots'][f'spell_level_{spell_level}'] = spell_level_remaining
        #Per mirar si tenen hit
    else:
        if 'damage' in fmenu123.selected_spell:
        #PER CALCULAR EL hit
            if fmenu123.selected_spell['damage']['hit'] == 0:
                #Sha de posar un while
                print("Usando sistema de hit")
                opcion = int(input("Tirada de hit:\n(0) Tirada normal\n(1) Tirada con ventaja\n(2) Tirada con desventaja\n"))
                if opcion == 0:
                    print("Tirando un solo dado...")
                    hit = dice.fdau(20) + variables['proficiency'] + ((variables['stats']['intelligence'] - 10) // 2)
                    print("Valor del hit es:", hit)
                elif opcion == 1:
                    print("Tirando dos dados...")
                    dado1 = dice.fdau(20)
                    dado2 = dice.fdau(20)
                    hit = max(dado1, dado2) + variables['proficiency'] + ((variables['stats']['intelligence'] - 10) // 2)
                    print("Valor del primer dado:", dado1)
                    print("Valor del segundo dado:", dado2)
                    print("Valor del hit es:", hit)
                elif opcion == 2:
                    print("Tirando dos dados...")
                    dado1 = dice.fdau(20)
                    dado2 = dice.fdau(20)
                    hit = min(dado1, dado2) + variables['proficiency'] + ((variables['stats']['intelligence'] - 10) // 2)
                    print("Valor del primer dado:", dado1)
                    print("Valor del segundo dado:", dado2)
                    print("Valor del hit es:", hit)
                else:
                    print("Opción inválida. Solo se acepta 0, 1 o 2.")
                #Tornar al menu
            elif fmenu123.selected_spell['damage']['hit'] == 1:
                spell_save_dc = 8 + variables['proficiency'] + ((variables['stats']['intelligence'] - 10) // 2)
                print(f"Ha de superar un valor de Spell save DC de {spell_save_dc} de {fmenu123.selected_spell['damage']['saving_throw']} ")
            else:
                #per si hi ha problema en el json
                print("Opción de sistema de hit no válida.")
            no_li_pega = 0
            if fmenu123.selected_spell['damage']['hit'] == 0:
                j = 0
                while j == 0:
                    li_pega = input(f"Ha hitejat amb el valor de hit {hit}? (S/N)")
                    if li_pega.lower() == "s":
                        j = 1     
                    elif li_pega.lower() == "n":
                        i = 1
                        print("Vaja el teu atac ha fallat")
                        menu12.fmenu12()
                    else:
                        print("Perdona no t'he entés.")
            elif fmenu123.selected_spell['damage']['hit'] == 1:
                j = 0
                while j == 0:
                    li_pega = input(f"S'ha salvat amb el valor de {spell_save_dc}? (S/N)")
                    if li_pega.lower() == "s":
                        j = 1      
                    elif li_pega.lower() == "n":
                        j = 1
                        no_li_pega = 1
                        print("S'ha salvat, anem a veure si es menja menys dany")
                    else:
                        print("Perdona no t'he entés.")

        #Això és el que serà per llençar els daus
            daditos = sum(lanzar_dados(fmenu123.selected_spell['damage']['damage_dice']))
            total_damage = daditos + int(variables['proficiency']) + ((int(variables['stats']['intelligence']) - 10) // 2)
            print(daditos, end=" + ")
            print(int(variables['proficiency']), end=" + ")
            print((int(variables['stats']['intelligence']) - 10) // 2, end=" + ")
            # If the requested spell level is higher than the spell's actual level, print a message and return None
            if spell_level > fmenu123.selected_spell['level']:
                #S'ha de posar el daño extra
                multiplicador = spell_level - fmenu123.selected_spell['level']
                for l in range(multiplicador):
                    sumita = sum(lanzar_dados(fmenu123.selected_spell['damage']['add_damage_x_level']))
                    total_damage += sumita
                    print(sumita, end=" + ")
                if no_li_pega == 1:
                    if fmenu123.selected_spell['damage']['half'] == 1:
                        total_damage /= 2
            print(f"Has fet {total_damage} de {fmenu123.selected_spell['damage']['damage_type']}")
            print()

        elif fmenu123.selected_spell['nombre'] == 'Shield':
            print(f"Tens un +5 al AC {variables['armor_class']} fins el començament del teu torn")    
        else:
            print(f"Has usado el hechizo {fmenu123.selected_spell['nombre']}")
        









#MENU 124 CANVIAR ELS SPELLS SLOTS MANUALMENT


def fmenu124():
    print("Hola")