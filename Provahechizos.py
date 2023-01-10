#La part del menu dels hechizos per tirar-los fa una llista de tots els hechizos enumerats
import json
import re
import dice
import menu12

# Carga el archivo JSON en un diccionario
with open("variables.json", "r") as f:
    variables = json.load(f)


def lanzar_dados(damage_dice):
    # Extraemos los números de la cadena
    resultado = re.findall(r'\d+', damage_dice)
    
    # Si no se encontraron dos números, devolvemos None
    if resultado is None:
        return None
    
    # Desempaquetamos la tupla
    veces, valor = resultado
    
    # Lanzamos los dados "veces" veces y guardamos los resultados en una lista
    return [dice.fdau(valor) for _ in range(veces)]


def use_spell(spell_name, spell_level):
   # Get the maximum and remaining number of spells for the given level
  spell_level_max = variables['spell_slots'][f'spell_level_{spell_level}_max']
  spell_level_remaining = variables['spell_slots'][f'spell_level_{spell_level}']

  # Return None if there are no remaining spells
  if spell_level_remaining == 0:
    print("No tienes mas hechizos de este nivel")
  else:
  # Decrement the number of remaining spells by 1
    spell_level_remaining -= 1

  # Update the number of remaining spells in the JSON data
  variables['spell_slots'][f'spell_level_{spell_level}'] = spell_level_remaining
  #PER CALCULAR EL hit
  if spell['damage']['hit'] == 0:
    print("Usando sistema de hit")
    opcion = input("Tirada de hit:\n(0) Tirada normal\n(1) Tirada con ventaja\n(2) Tirada con desventaja")
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
  elif spell['damage']['hit'] == 1:
    spell_save_dc = 8 + variables['proficiency'] + ((variables['stats']['intelligence'] - 10) // 2)
    print(f"Ha de superar un valor de Spell save DC de {spell_save_dc} de {spell['damage']['saving_throw']} ")
  else:
    print("Opción de sistema de hit no válida.")
  anem_al_damage = 0
  if spell['damage']['hit'] == 0:
    j = 0
    while j == 0:
      li_pega = input(f"Ha hitejat amb el valor de hit {hit}? (S/N)")
      if answer.lower() == "s":
          j = 1
          anem_al_damage = 1          
      elif answer.lower() == "n":
          i = 1
          menu12.fmenu12()
      else:
        print("Perdona no t'he entés.")
  elif spell['damage']['hit'] == 1:
    j = 0
    while j == 0:
      li_pega = input(f"S'ha salvat amb el valor de {spell_save_dc}? (S/N)")
      if answer.lower() == "s":
          j = 1
          anem_al_damage = 1          
      elif answer.lower() == "n":
          j = 1
          menu12.fmenu12()
      else:
        print("Perdona no t'he entés.")


  if anem_al_damage == 1:
    #Es posa el daño
    print("miaus")

  if spell_level == spell['level']:
    print(f'Hit: {spell["damage"]["hit"]}')
    print(f'Saving throw: {spell["damage"]["saving_throw"]}')
    print(f'Damage dice: {spell["damage"]["damage_dice"]}')
    print(f'Damage type: {spell["damage"]["damage_type"]}')
    total_damage = lanzar_dados(spell["damage"]["damage_dice"])
    print(total_damage)

   # If the requested spell level is higher than the spell's actual level, print a message and return None
  elif spell_level > spell['level']:
    #S'ha de posar el daño extra
    print('Overpowered!')










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
level = int(input(f"Ingresa el nivel del hechizo, el nivel base del hechizo es {selected_spell['level']}: "))

e = 0
while e == 0:
  # Verifica si el nivel ingresado es correcto
  if level >= selected_spell['level']:
    e = 1
    i = 0
    while i == 0:
      # Pide al usuario si quiere lanzar el hechizo
      answer = input(f"¿Quieres lanzar este {selected_spell['nombre']} de nivel {selected_spell['level']} ? (S/N) ")

    # Si el usuario quiere lanzar el hechizo, muestra la información de nuevo
      if answer.lower() == "s":
          print(f"Lanzando hechizo: {selected_spell['nombre']}")
          i = 1
          use_spell(selected_spell['nombre'],selected_spell['level'])
          
      # Si el usuario no quiere lanzar el hechizo, ejecuta la función fmenu124()
      elif answer.lower() == "n":
          fmenu123()
          i = 1
      else:
        print("Perdona no t'he entés.")
  else:
    e = 0
    print(f"Tienes que introducir un valor superior o igual a {selected_spell['level']}")

with open("variables.json", "w") as f:
  json.dump(variables, f)