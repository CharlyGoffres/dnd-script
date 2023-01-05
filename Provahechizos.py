#Menu de hechizos para ver los hechizos que tengo por nivel
import json

# Carga el archivo JSON en un diccionario
with open("variables.json", "r") as f:
    character = json.load(f)

# Obtiene la lista de hechizos
spells = character["hechizos"]

# Agrupa los hechizos según su nivel
spells_by_level = {}
for spell in spells:
    level = spell["level"]
    if level not in spells_by_level:
        spells_by_level[level] = []
    spells_by_level[level].append(spell)

# Imprime un menú con las secciones correspondientes a cada nivel de hechizo
print("Selecciona un hechizo:")
print()
for level, level_spells in spells_by_level.items():
    print(f"Nivel {level}:")
    for i, spell in enumerate(level_spells):
        print(f"  {i+1}. {spell['nombre']}")
print()








import json

# Load the JSON data into a Python object
with open('character.json', 'r') as f:
  character = json.load(f)

def use_spell(spell_name, spell_level):
  # Find the spell in the character's spell list
  spell = None
  for s in character['hechizos']:
    if s['nombre'] == spell_name:
      spell = s
      break

  # Return None if the spell was not found
  if spell is None:
    return None

  # If the requested spell level is higher than the spell's actual level, print a message and return None
  if spell_level > spell['level']:
    print('Overpowered!')
    return None

  # Get the maximum and remaining number of spells for the given level
  spell_level_max = character['spell_slots'][f'spell_level_{spell_level}_max']
  spell_level_remaining = character['spell_slots'][f'spell_level_{spell_level}']

  # Return None if there are no remaining spells
  if spell_level_remaining == 0:
    return None

  # Decrement the number of remaining spells by 1
  spell_level_remaining -= 1

  # Update the number of remaining spells in the JSON data
  character['spell_slots'][f'spell_level_{spell_level}'] = spell_level_remaining

  # If the requested spell level is the same as the spell's actual level, print the spell's details
  if spell_level == spell['level']:
    print(f'Hit: {spell["damage"]["hit"]}')
    print(f'Saving throw: {spell["damage"]["saving_throw"]}')
    print(f'Damage dice: {spell["damage"]["damage_dice"]}')
    print(f'Damage type: {spell["damage"]["damage_type"]}')

  # Return the spell object
  return spell







  #La part del menu dels hechizos per tirar-los
import json

# Carga el archivo JSON en un diccionario
with open("variables.json", "r") as f:
    character = json.load(f)

# Obtiene la lista de hechizos
spells = character["hechizos"]

# Imprime un menú con los nombres de los hechizos
print("Selecciona un hechizo:")
print()
for i, spell in enumerate(spells):
    print(f"{i+1}. {spell['nombre']}")
print()

# Pide al usuario que elija un hechizo
choice = int(input())

# Muestra la información del hechizo elegido
selected_spell = spells[choice - 1]
print()
print(f"Nombre: {selected_spell['nombre']}")
print(f"Nivel: {selected_spell['level']}")
print(f"Daño: {selected_spell['damage']}")